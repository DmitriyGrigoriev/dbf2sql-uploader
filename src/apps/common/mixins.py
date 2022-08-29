from django.db import models

from hashlib import sha256
from import_export.instance_loaders import CachedInstanceLoader
from src.config import settings

################################################################
# Mixin extend resource model and add some additional fields
################################################################
class ExtResource:
    """Extend resource model"""
    type = 'RESOURCE'
    database = None
    dest_connection = None

    hash_field_name = 'hash'
    hash_field_value = None

    class Meta:
        use_bulk = True
        batch_size = settings.BATCH_SIZE
        skip_unchanged = True
        # skip_diff = True
        # This flag can speed up imports
        # Cannot be used when performing updates
        # force_init_instance = True
        # This instance loader work only when there is one ``import_id_fields``
        import_id_fields = ('uid',)
        instance_loader_class = CachedInstanceLoader


    def before_import_row(self, row, row_number=None, **kwargs):
        if 'g071' in row and 'g072' in row and 'g073' in row:
            g07x = f"{row['g071']}/{row['g072'].strftime('%d%m%y')}/{row['g073']}"
            row['g07x'] = g07x

        if self.database is not None:
            row['database'] = self.database

        # Calculate row hash
        self.hash_field_value = sha256(repr(row.values()).encode('utf8')).hexdigest().encode('utf-8').decode('utf-8')
        row[self.hash_field_name] = self.hash_field_value

    # def skip_row(self, instance, original):
    #     skip = self.dest_connection.cursor().execute(
    #         f"SELECT [{self.hash_field_name}] FROM [{instance._meta.model_name}] WHERE [{self.hash_field_name}] = '{self.hash_field_value}'"
    #     ).fetchone()[0]
    #     return bool(skip)
        #return super(ExtResource, self).skip_row(instance, original)


##################################################################################
# SECTION: DBF export mixins
##################################################################################
class ExtBase(models.Model):
    """Extending base model table by additional fields"""
    g071 = models.CharField(max_length=8, primary_key=True)

    class Meta:
            abstract = True
            managed = False
            unique_together = (('g071', 'g072', 'g073'),)


class ExtBaseG32(models.Model):
    """Extending base model table by additional fields"""
    g071 = models.CharField(max_length=8, primary_key=True)

    class Meta:
            abstract = True
            managed = False
            unique_together = (('g071', 'g072', 'g073', 'g32'),)


class ExtBaseK32(models.Model):
    """Extending base model table by additional fields"""
    g071 = models.CharField(max_length=8, primary_key=True)

    class Meta:
            abstract = True
            managed = False
            unique_together = (('g071', 'g072', 'g073', 'k32'),)


##################################################################################
# SECTION: DBF import mixins
##################################################################################
class ExtSourceFields(models.Model):
    """Extending sql import table by additional fields"""
    uid = models.AutoField(primary_key=True)
    g071 = models.CharField(max_length=8, blank=True, null=True)
    # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    database = models.CharField(max_length=50, blank=True, null=True)
    g07x = models.CharField(max_length=23, blank=True, null=True)
    hash = models.CharField(max_length=64, blank=False, null=True,)
    # hash = models.CharField(max_length=64, blank=False, null=True, unique=True)
    docnum = models.CharField(db_column='DocNum', max_length=28, blank=True, null=True) # import from Doxc2sql
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['g07x']),
            models.Index(fields=['hash']),
        ]

##################################################################################
# SECTION: ARM Doc2Sql import mixins
##################################################################################
class ExtArmFields(ExtSourceFields):
    docnum = models.CharField(db_column='DocNum', max_length=28, blank=True, null=True)

    class Meta:
        abstract = True


class ExtNonUniqHash(ExtArmFields):
    """Extending sql import table by additional fields"""
    hash = models.CharField(max_length=64, blank=False, null=True)

    class Meta:
        abstract = True
        # indexes = [
        #     models.Index(fields=['g07x']),
        #     models.Index(fields=['hash']),
        # ]

##################################################################################
# SECTION: ARM Doc2Sql export mixins
##################################################################################
class ExtBaseDocNum(models.Model):
    """Extending base model table by additional fields"""
    docnum = models.CharField(db_column='DocNum', max_length=28, primary_key=True)
    g071 = models.CharField(max_length=8)

    class Meta:
            abstract = True
            managed = False
