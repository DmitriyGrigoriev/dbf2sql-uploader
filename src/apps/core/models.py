import logging
# from datetime import datetime
from django.db import models
from django.core.validators import validate_slug
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_dramatiq.models import Task
from src.apps.common.dataclasses import ETL

from .base.models import DefaultModel
from .managers import ImportTablesManager, ConnectSetManager
# from src.apps.common.functions import get_last_dbf_file_modify_date
# from src.apps.common.dataclasses import ImportInfo, RecordInfo
# from src.services.armcount import ARMCount

# Create your models here.

app_label = "core"

logger = logging.getLogger(__name__)

DEFAULT_ENGINE = 'django.db.backends.sqlite3'
DBF_ENGINE = 'src.db.connection.advantage'
MSSQL_ENGINE = 'mssql'


class ImportTables(DefaultModel):
    class Meta:
        db_table = 'import_tables'
        # Add verbose name
        verbose_name = '#3. Pipeline table'

    def __str__(self):
        return f"{self.connects}: {self.source_table} -> {self.dest_table}"

    connects = models.ForeignKey(
        to='ConnectSet',
        related_name='connect_sets',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Select conection')
    )
    source_table = models.CharField(max_length=50,
                                    verbose_name=_('Export table')
                                    )
    dest_table = models.CharField(max_length=50,
                                  verbose_name=_('Import table')
                                  )
    message_id = models.UUIDField(_('Redis message Id'), blank=True, null=True)
    uploadable = models.BooleanField(verbose_name='Uploadable', default=True)
    last_write = models.DateTimeField(verbose_name=_('Last write'), blank=True, null=True, )
    upload_record = models.IntegerField(verbose_name=_('Upload'), default=0)

    tables = ImportTablesManager()


class ConnectSet(DefaultModel):
    PIPE_TYPE = (
        (ETL.EXPORT.DBF, _('import from DBF')),
        (ETL.EXPORT.DOC2SQL, _('import from Doc2Sql')),
    )

    name = models.CharField(max_length=100)
    type = models.CharField(_('Select import type'), max_length=200,
                            choices=PIPE_TYPE, default=ETL.EXPORT.DBF, blank=False)
    source_conection = models.ForeignKey(
        to='ConnectWrapper',
        related_name='source_conection',
        on_delete=models.DO_NOTHING,
        verbose_name=_('Select source conection')
    )
    dest_conection = models.ForeignKey(
        to='ConnectWrapper',
        related_name='dest_conection',
        on_delete=models.DO_NOTHING,
        verbose_name=_('Select destination conection')
    )
    enabled = models.BooleanField(default=True)

    consets = ConnectSetManager()

    class Meta:
        db_table = 'connect_set'
        # Add verbose name
        verbose_name = '#2. Pipeline'

    def __str__(self):
        return self.name


class ConnectWrapper(DefaultModel):
    """Store data source info like as connection string"""
    CONNECTOR_ENGINE = (
        # (DEFAULT_ENGINE, _('SQLite')),
        (DBF_ENGINE, _('DBF')),
        (MSSQL_ENGINE, _('MSSQL')),
    )
    conname = models.CharField(_('Connect name'), max_length=128, blank=False, unique=True, validators=[validate_slug])
    slug_name = models.SlugField(max_length=150)
    engine = models.CharField(_('Select engine'), max_length=200,
                              choices=CONNECTOR_ENGINE, default=MSSQL_ENGINE, blank=False)
    description = models.TextField(_('Description'), max_length=200, blank=True)
    is_active = models.BooleanField(_('Active'), default=True)
    name = models.CharField(max_length=250, verbose_name=_('NAME'), blank=False)
    options = models.TextField(verbose_name=_('Connect options'))
    user = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=100, blank=True)
    host = models.CharField(verbose_name=_('HOST'), max_length=100, blank=True)
    port = models.PositiveIntegerField(verbose_name=_('PORT'), blank=True, null=True)

    # options = models.ForeignKey(
    #     to='ConnectPropertyWrapper',
    #     related_name='connect_options',
    #     on_delete=models.CASCADE,
    #     verbose_name=_('Connect options')
    # )

    @classmethod
    def get_slug_name(self, conname: str = None) -> str:
        if conname:
            slug_name = slugify(conname)
        else:
            raise ValueError(_("Method ConnectWrapper.get_slug_name() require parameter for generate out value"))
        return slug_name

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug_name = self.get_slug_name(self.conname)
        super(ConnectWrapper, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using, update_fields=update_fields
        )

    class Meta:
        db_table = 'connects'
        constraints = [
            models.UniqueConstraint(
                fields=["engine", "name"],
                name="unique_database_name"
            )
        ]
        # Add verbose name
        verbose_name = '#1. Connection list'

    def __str__(self):
        return self.conname
