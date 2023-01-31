import uuid
import logging
from hashlib import sha256

from django.db import models
from import_export.instance_loaders import CachedInstanceLoader

from import_export import resources
from src.apps.common.dataclasses import ETL
# from src.apps.core.models import ConnectSet
from django.db import connections
# from src.apps.navision.models import NlcCustomer
from src.services.base.baseimport import get_databases_item_value

logger = logging.getLogger(__name__)


class ExtModelDeclarativeMetaclass(resources.ModelDeclarativeMetaclass):

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)

        opts = new_class._meta

        setattr(opts, 'redis_message_id', None)
        setattr(opts, 'poll_pk', -1)
        setattr(opts, 'database', '*')
        setattr(opts, 'params', None)

        return new_class

    def get_database(cls):
        # Meta property
        # self.database = get_databases_item_value(alias=self.params.source_connection_name).lower()
        pass
        # cls.opts._meta.poll_pk = cls.params.poll_pk
        # cls.opts._meta.using_db = cls.params.dest_connection_name
        # resource_model._meta.database = get_databases_item_value(alias=resource_model._meta.using_db)



################################################################
# Mixin extend resource model and add some additional fields
################################################################
class ExtResource(resources.ModelResource, metaclass=ExtModelDeclarativeMetaclass):
    """Extend resource model"""

    type = "RESOURCE"  # using as marker for resource class
    # database = None

    class Meta(resources.ResourceOptions):
        using_db = None
        use_bulk = True
        batch_size = ETL.BULK.BATCH_SIZE
        # skip_unchanged = False
        skip_diff = False
        # skip_unchanged = True
        # skip_diff = True
        # This flag can speed up imports
        # Cannot be used when performing updates
        # force_init_instance = True
        # This instance loader work only when there is one ``import_id_fields``
        import_id_fields = ("uid",)
        instance_loader_class = CachedInstanceLoader

    def bulk_create(self, using_transactions, dry_run, raise_errors, batch_size=None):
        """
        Creates objects by calling ``bulk_create``.
        !Important: override original bulk_create, added using
        """
        try:
            if len(self.create_instances) > 0:
                if not using_transactions and dry_run:
                    pass
                else:
                    # database = get_databases_item_value(alias=self._meta.using_db)
                    self._meta.model.objects.using_db = self._meta.using_db
                    self._meta.model.objects._db = self._meta.using_db
                    # self._meta.model.objects.using_db = ConnectSet.consets.record(pk=self._meta.poll_pk).dest_conection.slug_name
                    # self._meta.database = get_databases_item_value(alias=self._meta.model.objects.using_db)
                    logger.info(
                        f'###### BULK INSERT INTO: {get_databases_item_value(alias=self._meta.model.objects.using_db)}.{self._meta.model._meta.db_table} '
                        f'## Redis message id: {self._meta.redis_message_id} ##'
                    )
                    # logger.info(
                    #     f'###### DATABASES.NAME: {self._meta.database} ######'
                    # )
                    self._meta.model.objects.bulk_create(self.create_instances, batch_size=batch_size)
                    # self._meta.model.objects.using(self._meta.using_db)\
                    #     .bulk_create(self.create_instances, batch_size=batch_size)
        except Exception as e:
            logger.exception(e)
            if raise_errors:
                raise e
        finally:
            self.create_instances.clear()

    def before_import_row(self, row, row_number=None, **kwargs):

        # params: ImportInfo = self._meta.params
        g07x: str = None

        if (
            ETL.FIELD.G071 in row
            and ETL.FIELD.G072 in row
            and ETL.FIELD.G073 in row
        ):
            g07x = f"{row[ETL.FIELD.G071]}/{row[ETL.FIELD.G072].strftime('%d%m%y')}/{row[ETL.FIELD.G073]}"
            row[ETL.FIELD.G07X] = g07x

        # Implement logic from pDCLHeadAdded
        # UPDATE [LocalFTS].[dbo].[tDCLHEAD] Set G081=G141, G082=G142, G087=G147
        # 		WHERE g081 is null AND g082 is null AND G011='ИМ';
        if ETL.MAINTABLES.DCLHEAD.lower() in self._meta.model._meta.db_table.lower():
            if row[ETL.FIELD.G081] is None and row[ETL.FIELD.G082] is None and row[ETL.FIELD.G011] == "ИМ":
                self.update_field(row, ETL.FIELD.G081, ETL.FIELD.G141, "ИМ")
                self.update_field(row, ETL.FIELD.G082, ETL.FIELD.G142, "ИМ")
                self.update_field(row, ETL.FIELD.G087, ETL.FIELD.G147, "ИМ")

            # if there isn't value trying to get it from the NAVISION database
            if row[ETL.FIELD.G081] is None and row[ETL.FIELD.G011] == "ИМ" and g07x:
                inn_no = self.get_nav_inn(g07x) or None
                row[ETL.FIELD.G081] = inn_no

            if row[ETL.FIELD.G081] is None and row[ETL.FIELD.G082] is None and row[ETL.FIELD.G011] == "ЭК":
                self.update_field(row, ETL.FIELD.G021, ETL.FIELD.G141, "ЭК")
                self.update_field(row, ETL.FIELD.G022, ETL.FIELD.G142, "ЭК")
                self.update_field(row, ETL.FIELD.G027, ETL.FIELD.G147, "ЭК")

            if row[ETL.FIELD.G021] is None and row[ETL.FIELD.G011] == "ЭК" and g07x:
                inn_no = self.get_nav_inn(g07x) or None
                row[ETL.FIELD.G021] = inn_no

        if self.type:
            row[ETL.FIELD.EXPTYPE] = self.type

        if self._meta.database:
            row[ETL.FIELD.DATABASE] = self._meta.database
        # if self._meta.using_db:
        #     row[ETL.FIELD.DATABASE] = get_databases_item_value(alias=self._meta.using_db)
        # if self._meta.using_db:
        #     row[ETL.FIELD.DATABASE] = get_databases_item_value(alias=self._meta.using_db)

        row[ETL.FIELD.HASH] = self.calculate_hash(row)

        # Replace value in field GD0 if NULL to ''
        if ETL.FIELD.GD0 in row and row[ETL.FIELD.GD0] is None:
            row[ETL.FIELD.GD0] = ''

    def calculate_hash(self, row):
        # Calculate row hash
        return (
            sha256(repr(row.values()).encode("utf8"))
            .hexdigest()
            .encode("utf-8")
            .decode("utf-8")
        )

    def update_field(self, record, source: str, dest: str, type: str) -> None:
        if (
            source in record
            and dest in record
            and ETL.FIELD.G011 in record
        ):
            if record[ETL.FIELD.G011] == type and (
                record[source] is None or record[source].replace(' ', '') == ''
            ):
                record[source] = record[dest]

    # def skip_row(self, instance, original):
    #     skip = self.dest_connection.cursor().execute(
    #         f"SELECT [{self.hash_field_name}] FROM [{instance._meta.model_name}] WHERE [{self.hash_field_name}] = '{self.hash_field_value}'"
    #     ).fetchone()[0]
    #     return bool(skip)
    # return super(ExtResource, self).skip_row(instance, original)


    def get_nav_inn(self, dt_no: str):
        ######################################################################
        # Return INN from NAVISION database
        #######################################################################
        sql = (f"\n"
               f"SELECT CustomerNo.[VAT Registration No_] i"
               f" 	FROM ("
               f" 			SELECT DISTINCT [GTDNo_] G07X, [Customer No_] DTNo"
               f" 				FROM [NLC$GTD Ledger Entry]"
               f" 		  ) GTDNo"
               f" 	JOIN [NLC$Customer] CustomerNo ON CustomerNo.No_=GTDNo.DTNo"
               f" WHERE GTDNo.G07X='{dt_no}'"
               )
        inn_no = self.execute_custom_sql(connection_name=ETL.CONNECT.NAVISION, sql=sql)

        return inn_no


    def execute_custom_sql(self, connection_name: str, sql: str):
        # self.print(f"\n################## Execute select statement: {sql}  ##################")
        with connections[connection_name].cursor() as cursor:
            cursor.execute(sql)
            row = cursor.fetchone()
        return row

class ArmResource(ExtResource):
    """Generate unique hash for each record from Doc2SQL"""

    def calculate_hash(self, row):
        # Calculate row hash
        salt = str(uuid.uuid4()).encode("utf8")
        return (
            sha256(salt + repr(row.values()).encode("utf8"))
            .hexdigest()
            .encode("utf-8")
            .decode("utf-8")
        )


##################################################################################
# SECTION: DBF export mixins
##################################################################################
class NsiBase(models.Model):
    """Extending base model table by additional fields"""

    g071 = models.CharField(max_length=8, primary_key=True)

    class Meta:
        abstract = True
        managed = False

class ExtBase(models.Model):
    """Extending base model table by additional fields"""

    g071 = models.CharField(max_length=8, primary_key=True)

    class Meta:
        abstract = True
        managed = False
        unique_together = (("g071", "g072", "g073"),)


class ExtBaseG32(models.Model):
    """Extending base model table by additional fields"""

    g071 = models.CharField(max_length=8, primary_key=True)

    class Meta:
        abstract = True
        managed = False
        unique_together = (("g071", "g072", "g073", "g32"),)


class ExtBaseK32(models.Model):
    """Extending base model table by additional fields"""

    g071 = models.CharField(max_length=8, primary_key=True)

    class Meta:
        abstract = True
        managed = False
        unique_together = (("g071", "g072", "g073", "k32"),)


##################################################################################
# SECTION: DBF import mixins
##################################################################################
class BaseSourceFields(models.Model):
    unique_hash = True

    uid = models.AutoField(primary_key=True)
    # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sourcetype = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        db_index=True,
    )
    database = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        db_index=True,
    )

    class Meta:
        abstract = True

class ExtSourceFields(BaseSourceFields):
    """Extending sql import table by additional fields"""

    g071 = models.CharField(max_length=8, blank=True, null=True)
    # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    g07x = models.CharField(
        max_length=23,
        blank=True,
        null=True,
        db_index=True,
    )
    # hash = models.CharField(max_length=64, blank=False, null=True,)
    hash = models.CharField(max_length=64, blank=False, null=True, unique=True)
    docnum = models.CharField(
        db_column="DocNum", max_length=28, blank=True, null=True
    )  # import from Doxc2sql
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=["g07x"]),
            models.Index(fields=["hash"]),
        ]

    # def save(
    #     self, force_insert=False, force_update=False, using=None, update_fields=None
    # ):
    #     super().save(force_insert=False, force_update=False, using=self._meta.model.objects.db, update_fields=None)


class ExtSourceNoHashUniqueIndex(ExtSourceFields):
    unique_hash = False

    hash = models.CharField(
        max_length=64,
        blank=False,
        null=True,
        db_index=True,
    )

    class Meta(ExtSourceFields.Meta):
        abstract = True


##################################################################################
# SECTION: ARM Doc2Sql import mixins
##################################################################################
class ExtArmFields(ExtSourceFields):
    docnum = models.CharField(
        db_column="DocNum", max_length=28, blank=True, null=True
    )

    class Meta:
        abstract = True


# class ExtNonUniqHash(ExtArmFields):
#     """Extending sql import table by additional fields"""
#     hash = models.CharField(max_length=64, blank=False, null=True,db_index=True,)
#
#     class Meta:
#         abstract = True
#         # indexes = [
#         #     models.Index(fields=['g07x']),
#         #     models.Index(fields=['hash']),
#         # ]

##################################################################################
# SECTION: ARM Doc2Sql export mixins
##################################################################################
class ExtBaseDocNum(models.Model):
    """Extending base model table by additional fields"""

    docnum = models.CharField(
        db_column="DocNum", max_length=28, primary_key=True
    )
    g071 = models.CharField(max_length=8)

    class Meta:
        abstract = True
        managed = False
