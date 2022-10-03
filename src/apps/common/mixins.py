import uuid
from hashlib import sha256

from django.db import models
from import_export.instance_loaders import CachedInstanceLoader

from src.apps.common.dataclasses import ETL


################################################################
# Mixin extend resource model and add some additional fields
################################################################
class ExtResource:
    """Extend resource model"""

    type = "RESOURCE"  # using as marker for resource class
    database = None

    class Meta:
        use_bulk = True
        batch_size = ETL.BULK.BATCH_SIZE
        skip_unchanged = True
        # skip_diff = True
        # This flag can speed up imports
        # Cannot be used when performing updates
        # force_init_instance = True
        # This instance loader work only when there is one ``import_id_fields``
        import_id_fields = ("uid",)
        instance_loader_class = CachedInstanceLoader

    def before_import_row(self, row, row_number=None, **kwargs):
        if (
            ETL.FIELD.G071 in row
            and ETL.FIELD.G072 in row
            and ETL.FIELD.G073 in row
        ):
            g07x = f"{row[ETL.FIELD.G071]}/{row[ETL.FIELD.G072].strftime('%d%m%y')}/{row[ETL.FIELD.G073]}"
            row[ETL.FIELD.G07X] = g07x

        if self.type:
            row[ETL.FIELD.EXPTYPE] = self.type

        if self.database:
            row[ETL.FIELD.DATABASE] = self.database

        row[ETL.FIELD.HASH] = self.calculate_hash(row)

    def calculate_hash(self, row):
        # Calculate row hash
        return (
            sha256(repr(row.values()).encode("utf8"))
            .hexdigest()
            .encode("utf-8")
            .decode("utf-8")
        )

    # def skip_row(self, instance, original):
    #     skip = self.dest_connection.cursor().execute(
    #         f"SELECT [{self.hash_field_name}] FROM [{instance._meta.model_name}] WHERE [{self.hash_field_name}] = '{self.hash_field_value}'"
    #     ).fetchone()[0]
    #     return bool(skip)
    # return super(ExtResource, self).skip_row(instance, original)


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
class ExtSourceFields(models.Model):
    """Extending sql import table by additional fields"""
    unique_hash = True

    uid = models.AutoField(primary_key=True)
    g071 = models.CharField(max_length=8, blank=True, null=True)
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
