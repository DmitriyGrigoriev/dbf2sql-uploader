import os
import logging
from datetime import datetime, timezone

from django.db import models
from django.core.validators import validate_slug, validate_ipv4_address
from django.utils.text import slugify
from .base.models import DefaultModel
from django.utils.translation import gettext_lazy as _
from src.config import settings
from src.apps.common.dataclasses import ImportInfo
from django_dramatiq.models import Task

# Create your models here.

app_label = "core"

logger = logging.getLogger(__name__)

DEFAULT_ENGINE = 'django.db.backends.sqlite3'
DBF_ENGINE = 'src.db.connection.advantage'
MSSQL_ENGINE = 'mssql'


class ImportTablesManager(models.Manager):
    def tables_for_import(self, connection_pull_pk):
        return self.filter(
            connects=connection_pull_pk,
            connects__enabled=True,
            uploadable=True).all()

    def tables_import_info_list(self, poll_pk) -> ImportInfo:
        """
        Return list of tables which have file last write time different from imported last time

        :param poll_pk:
        :return ImportInfo:
                -----------------------------
                table_pk: int,
                object_pk: int,
                source_connection_name: str,
                source_table_name: str,
                dest_connection_name: str,
                dest_table_name: str,
                type: str
                ------------------------------
        """
        connection_poll = ConnectSet.consets.record(pk=poll_pk)
        source_connection_name = connection_poll.source_conection.slug_name
        dest_connection_name = connection_poll.dest_conection.slug_name
        t_list = [
            ImportInfo(
                t.pk,
                connection_poll.pk,
                source_connection_name,
                t.source_table,
                dest_connection_name,
                t.dest_table,
                connection_poll.source_conection.name,
                connection_poll.type # import type: DBF / ARM
            )
            for t in ImportTables.tables.tables_for_import(connection_poll.pk) \
            if self.dbf_last_write(connection_poll.source_conection.name, t.source_table) != t.last_write
                # and self.approved_task_status(t.message_id)
        ]
        return t_list


    def table_import_info(self, table_pk) -> ImportInfo:
        """Fill kwargs dict by data"""
        t = ImportTables.tables.filter(pk=table_pk).get()
        t_list = [
            ImportInfo(
                t.pk,
                t.connects.pk,
                t.connects.source_conection.slug_name,
                t.source_table,
                t.connects.dest_conection.slug_name,
                t.dest_table,
                t.dest_table,
                t.connects.type # import type: DBF / ARM
            )
        ]
        return t_list

    # def get_kwargs(self, table_pk) -> dict:
    #     """Fill kwargs dict by data"""
    #     table = ImportTables.tables.filter(pk=table_pk).get()
    #     kwargs={
    #         "table_pk": table.pk,
    #         "poll_pk": table.connects.pk,
    #         "source_connection_name": table.connects.source_conection.slug_name,
    #         "source_table_name": table.source_table,
    #         "dest_connection_name": table.connects.dest_conection.slug_name,
    #         "dest_table_name": table.dest_table
    #     }
    #     return kwargs

    # def current_task_status(self, message_id) -> str or None:
    #     return Task.tasks.filter(pk=message_id).get().status if message_id else None
    #
    # def approved_task_status(self, message_id) -> str or None:
    #     status = self.current_task_status(message_id)
    #     return True if status == STATUS_DONE or status is None else False

    def dbf_last_write(self, data_directory, file_name)-> datetime:
        fname = f"{data_directory}{file_name}.DBF"
        last_write = None
        if os.path.isfile(fname):
            last_write = datetime.fromtimestamp(os.path.getmtime(fname), tz=timezone.utc)
        return last_write

    def update_last_import_date(self, message_data, result):
        """Update the date and time of last write uploaded data from the import table"""
        databases = settings.DATABASES
        kwargs = message_data['kwargs']
        table_pk = kwargs['table_pk']
        message_id = message_data['message_id']
        source_databases = databases[kwargs['source_connection_name']]

        print("################################################################################")
        print(f"############ Message id {message_id} is success ########")
        print("################################################################################")
        #logger.info(f"############ Received message Id: {message_id} ############")

        if source_databases:
            data_directory = source_databases["NAME"]
            source_table = f"{kwargs['source_table_name']}"
            # Get last write file date
            last_write = self.dbf_last_write(data_directory, source_table)
            print("################################################################################")
            print(f"#### File {data_directory}{source_table}.DBF last write was at {last_write}  ####")
            print("################################################################################")
            record_to_update = ImportTables.tables.filter(pk=table_pk)
            if last_write:
                # last_write = datetime.fromtimestamp(last_write_time, tz=pytz.timezone(settings.TIME_ZONE)).strftime('%Y-%m-%d %H:%M:%S')
                record_to_update.update(last_write=last_write)
            if result:
                print("#########################################################")
                print(f"############ Has been imported {result} records ########")
                print("#########################################################")
                record_to_update.update(upload_record=result)
            # Update import_table redis message id
            record_to_update.update(message_id=message_id)


class ImportTables(DefaultModel):
    class Meta:
        db_table = 'import_tables'
        # Add verbose name
        verbose_name = '3. Pipeline table'

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
    uploadable = models.BooleanField(default=True)
    last_write = models.DateTimeField(verbose_name=_('Last write'), blank=True, null=True,)
    upload_record = models.IntegerField(verbose_name=_('Upload'), default=0)

    tables = ImportTablesManager()



class ConnectSetManager(models.Manager):
    def record(self, pk):
        return self.filter(pk=pk).get()

    def allowed_for_import(self):
        return self.filter(enabled=True).all()

class ConnectSet(DefaultModel):
    PIPE_TYPE = (
        ('DBF', _('import from DBF')),
        ('ARM', _('import from Doc2Sql')),
    )

    name = models.CharField(max_length=100)
    type = models.CharField(_('Select import type'), max_length=200,
                                 choices=PIPE_TYPE, default='DBF', blank=False)
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
        verbose_name = '2. Pipeline'


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
    port = models.PositiveIntegerField(verbose_name=_('PORT'), blank=True, default=0)

    # options = models.ForeignKey(
    #     to='ConnectPropertyWrapper',
    #     related_name='connect_options',
    #     on_delete=models.CASCADE,
    #     verbose_name=_('Connect options')
    # )

    @classmethod
    def get_slug_name(self, conname: str=None) -> str:
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
                fields=["engine","name"], name="unique_database_name"
            )
        ]
        # Add verbose name
        verbose_name = '1. Connection list'

    def __str__(self):
        return self.conname

