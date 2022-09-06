import os
import inspect
import logging
from pathlib import Path
from importlib import import_module
from import_export import resources
from django.db import connections
from django.utils.connection import ConnectionDoesNotExist
from django.utils.module_loading import module_has_submodule
from django.db import models
from src.apps.common.dataclasses import ETL
from src.config import settings

logger = logging.getLogger(__name__)


class BaseImport:
    _limit = ETL.BULK.BATCH_SIZE

    def __init__(self) -> None:

    # def __init__(self, source_connection_name: str, source_table_name: str,
    #              dest_connection_name: str, dest_table_name: str, logger=None,
    #              mode: str = ETL.MODE.FULL
    #              ) -> None:

        self._type = None
        self._source_connection_name = None
        self._dest_connection_name = None
        self._source_model = None
        self._dest_model = None
        self._reccount = 0

        self._source_model_module = None
        self._dest_model_module = None

        self.source_model = None
        self.dest_model = None
        self.resources = {}

        self._logger = None
        self._mode = None

        self._headers = None

    @property
    def source_model_module(self):
        return self._source_model_module

    @source_model_module.setter
    def source_model_module(self, value):
        self._source_model_module = value

    @property
    def dest_model_module(self):
        return self._dest_model_module

    @dest_model_module.setter
    def dest_model_module(self, value):
        self._dest_model_module = value

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        self._headers = value

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, value):
        self._logger = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def source_connection_name(self):
        return self._source_connection_name

    @source_connection_name.setter
    def source_connection_name(self, value):
        self._source_connection_name = value
        if self.source_model:
            self.source_model._meta.model.objects._db = self.source_connection_name

        if self.source_connection_name:
            self.source_connection = self.get_connection_by_alias(self.source_connection_name)

    @property
    def source_model(self):
        return self._source_model

    @source_model.setter
    def source_model(self, value):
        """Set property to the source model and define what connect we will be using farther"""
        self._source_model = value
        if self.source_model:
            self.headers = self._get_exported_headers()

        if self.source_connection_name:
            self.source_model._meta.model.objects._db = self.source_connection_name

    @property
    def dest_model(self):
        return self._dest_model

    @dest_model.setter
    def dest_model(self, value):
        self._dest_model = value
        if self.dest_connection_name:
            self.dest_model._meta.model.objects._db = self.dest_connection_name

    @property
    def dest_connection_name(self):
        return self._dest_connection_name

    @dest_connection_name.setter
    def dest_connection_name(self, value: str):
        self._dest_connection_name = value
        if self.dest_model:
            self.dest_model._meta.model.objects._db = self._dest_connection_name

        if self.dest_connection_name:
            self.dest_connection = self.get_connection_by_alias(self.dest_connection_name)

    def restore_default(
            self, source_connection_name: str, source_table_name: str,
            dest_connection_name: str, dest_table_name: str, logger=None,
            mode: str = ETL.MODE.FULL
    ) -> None:

        self.source_connection_name = source_connection_name
        self.source_table_name = source_table_name
        self.dest_connection_name = dest_connection_name
        self.dest_table_name = dest_table_name
        self.logger = logger
        self.mode = mode

    def get_source_model_class(self):
        return self.get_model_class(
            self.source_model_module, 'models', self.source_table_name
        )

    def get_dest_model_class(self):
        return self.get_model_class(
            self.dest_model_module, 'models', self.dest_table_name
        )

    def get_resources(self):
        ###########################################################################
        # First setting connection and then attach using_db to source model
        ###########################################################################
        self.source_model = self.get_source_model_class()

        ###########################################################################
        # First setting connection and then attach using_db to destination model
        ###########################################################################
        self.dest_model = self.get_dest_model_class()

        self.resources = dict(
            self.get_list_classes(
                ETL.PIPE_MODULES.DBF_IMPORT if self.type == ETL.EXPORT.DBF else ETL.PIPE_MODULES.DOC2SQL_IMPORT,
                ETL.PIPE_MODULES.DBF_RESOURCE if self.type == ETL.EXPORT.DBF else ETL.PIPE_MODULES.DOC2SQL_RESOURCE,
                resources.ModelResource
            )
        )


    def print(self, message) -> None:
        if self.logger:
            self.logger.info(message)
        else:
            print(message)

    def _get_real_database_name(self):
        return settings.DATABASES[self.source_connection_name]['NAME']

    def _get_real_localfts_name(self):
        return settings.DATABASES[ETL.CONNECT.LOCALFTS]["NAME"]

    def _get_real_source_table_name(self):
        return self.source_model._meta.db_table

    def _get_real_dest_table_name(self):
        return self.dest_model._meta.db_table

    def _get_resource_models(self) -> resources.ModelResource:
        for name, model in self.resources.items():
            if model.Meta.model.__name__.lower() == self.dest_model._meta.model.__name__.lower():
                return model()
        return None

    def _get_exported_headers(self) -> list:
        """Return fields list from model"""
        return [field.attname.lower() for field in self.source_model._meta.fields]

    def _get_imported_headers(self) -> list:
        """Return fields list from model"""
        return [field.attname for field in self.dest_model._meta.fields]

    def _get_source_database_id(self) -> str:
        """
        Extract dir from settings.DATABASES[][NAME]
        Return "NAME": "\\192.168.0.122\BASES\GTD_2022_LG"

        :return: DBF data directory name
        """
        try:
            return self.get_databases_item_value(
                alias=self.source_connection_name,
                key='NAME'
            ).lower()
        except AttributeError:
            raise

    def _create_resource_instance(self):
        res_model = self._get_resource_models()
        try:
            res_model.type = self.type
            res_model.database = self._get_source_database_id()
            # res_model.dest_connection = self.dest_connection
        except AttributeError:
            pass
        return res_model

    def _execute_query(self, row_sql: str, params=None) -> list:
        """Return rows by executing query SELECT * from dbf_model"""
        return self.source_connection.cursor().execute(row_sql, params)

    def get_connection_by_alias(self, alias: str) -> connections:
        """Check connection using the connection name, see DATABASES section"""
        try:
            if alias in connections:
                return connections[alias]
            else:
                raise ConnectionDoesNotExist(alias)
        except Exception as e:
            logger.exception(e)
            raise e

    def get_databases_item_value(self, alias: str, key: str) -> str:
        """Return value from settings.DATABASES dict"""
        if alias is None:
            alias = "default"

        if alias in settings.DATABASES:
            data_dir_or_file = settings.DATABASES[alias][key]
            db_item_value = os.path.basename(data_dir_or_file)
            if db_item_value == '':
                db_item_value = Path(data_dir_or_file).parts[-1]
            return db_item_value

        return None

    def get_list_classes(self, entry, module_name, base_class) -> list:

        try:
            app_module = import_module(entry)
        except Exception as e:
            logger.exception(e)
            raise e

        res_models = []

        if module_has_submodule(app_module, module_name):
            mod_path = "%s.%s" % (entry, module_name)
            mod = import_module(mod_path)
            # Check if there's exactly one AppConfig candidate,
            # excluding those that explicitly define default = False.

            res_models = [
                (name, candidate)
                for name, candidate in inspect.getmembers(mod, inspect.isclass)
                if (
                        issubclass(candidate, base_class) and candidate is not base_class \
                        and hasattr(candidate, 'type')
                )
            ]

        return res_models

    def _get_export_raw_sql(self) -> str:
        """Return raw sql for export model"""
        return self.source_model.__class__.objects.all().query.__str__()

    def get_list_tables_from_model_class(self, entry: str, module_name: str) -> list:
        """Return list of table names selected in the db_table property Meta class"""
        return [klass._meta.db_table for _, klass in self.get_list_classes(entry, module_name, models.Model)]

    def get_model_class(self, entry: str, module_name: str, db_table: str) -> models:
        """Return model associated with the db_table property Meta class"""
        return [
                   klass for _, klass in self.get_list_classes(entry, module_name, models.Model)
                   if (
                    klass._meta.db_table.lower() == db_table.lower()
            )
               ][0]() or None

    def _get_sql_fields_list(self) -> str:
        fields_set = [f.name for f in self.source_model._meta.fields if f.name != self.source_model._meta.pk.name]
        fields = ""
        for f in fields_set:
            fields += f"[{f}], "
        # remove 2 last symbols
        result = fields[0:-2]
        return result

    # def _get_table_prefix(self, type):
    #     try:
    #         prefix = settings.PIPE_MODULES[type]['table_prefix'].lower()
    #     except AttributeError:
    #         prefix = ''
    #     return prefix

    def _delete_all_imported_records(self, model: models) -> bool:
        # clearing down existing objects
        try:
            sql = f"TRUNCATE TABLE {model._meta.db_table}"
            self.dest_connection.cursor().execute(sql)
            # model.__class__.objects.using(self.dest_connection.alias).all().delete()
        except Exception as e:
            logger.exception(e)
            raise e

        return True
