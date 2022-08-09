# import uuid
from django.db import models
from import_export.instance_loaders import CachedInstanceLoader
from src.config import settings

class ExtResource:
    database = None

    class Meta:
        use_bulk = True
        batch_size = settings.BATCH_SIZE
        skip_unchanged = True
        #skip_diff = True
        # This flag can speed up imports
        # Cannot be used when performing updates
        # force_init_instance = True
        # This instance loader work only when there is one ``import_id_fields``
        import_id_fields = ('uid',)
        instance_loader_class = CachedInstanceLoader


    def before_import_row(self, row, row_number=None, **kwargs):
        if 'g071' in row and 'g072' in row and 'g073' in row:
            year, mounth, day = row['g072'].split('-')
            g07x = f"{row['g071']}/{day + mounth + year[2:]}/{row['g073']}"
            row['g07x'] = g07x

        if self.database is not None:
            row['database'] = self.database


class ExtSourceFields(models.Model):
    """Extending sql import table by additional fields"""
    uid = models.AutoField(primary_key=True)
    g071 = models.CharField(max_length=8, blank=True, null=True)
    # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    database = models.CharField(max_length=50, blank=True, null=True)
    g07x = models.CharField(max_length=23, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True