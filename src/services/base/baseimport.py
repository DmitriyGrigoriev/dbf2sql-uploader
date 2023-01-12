import os
import copy
import inspect
import datetime
from dateutil.relativedelta import relativedelta
from importlib import import_module
from pathlib import Path

from django.db import connections, models
from django.utils.connection import ConnectionDoesNotExist
from django.utils.module_loading import module_has_submodule
from import_export import resources

from src.apps.common.dataclasses import ETL, ImportInfo
from src.config import settings

from dramatiq.logging import get_logger

# logger = logging.getLogger(__name__)


def get_databases_item_value(alias: str, key: str = "NAME") -> str:
    """Return value from settings.DATABASES[] dict"""
    if alias is None:
        alias = "default"

    if alias in settings.DATABASES:
        data_dir_or_file = settings.DATABASES[alias][key]
        db_item_value = os.path.basename(data_dir_or_file)
        if db_item_value == "":
            db_item_value = Path(data_dir_or_file).parts[-1]
        return db_item_value

    return ""


class BaseImport:
    def __init__(self, params: ImportInfo) -> None:
        self.params = self.get_copy_params(params)
        self._type = self.params.type
        self._source_connection_name = None
        self._dest_connection_name = None
        self._source_model = None
        self._dest_model = None
        self._reccount = 0

        self._limit = ETL.BULK.BATCH_SIZE
        self._period_of_month = ETL.BULK.SHIFT_MONTHS  # get export data for 10 last month
        self._redis_message_id = self.params.redis_message_id

        self._source_model_module = None
        self._dest_model_module = None

        self.source_model = None
        self.dest_model = None
        self.resources: dict = {}

        self.logger = get_logger(__name__, type(self))
        self._headers = None

        # There are definitions of the class model
        if self.type == ETL.EXPORT.DBF:
            self.source_model_module = ETL.PIPE_MODULES.DBF_EXPORT
            self.dest_model_module = ETL.PIPE_MODULES.DBF_IMPORT

        if self.type == ETL.EXPORT.DOC2SQL:
            self.source_model_module = ETL.PIPE_MODULES.DOC2SQL_EXPORT
            self.dest_model_module = ETL.PIPE_MODULES.DOC2SQL_IMPORT

        if self.type == ETL.EXPORT.DBF and self.params.dest_connection_name == ETL.CONNECT.LOCALFTS:
            self.source_model_module = ETL.PIPE_MODULES.DBF_IMPORT
            self.dest_model_module = ETL.PIPE_MODULES.DBF_IMPORT

        if self.type == ETL.EXPORT.DOC2SQL and self.params.dest_connection_name == ETL.CONNECT.LOCALFTS:
            self.source_model_module = ETL.PIPE_MODULES.DOC2SQL_IMPORT
            self.dest_model_module = ETL.PIPE_MODULES.DBF_IMPORT

        self.source_table_name = self.params.source_table_name
        self.dest_table_name = self.params.dest_table_name

        self.source_connection_name = self.params.source_connection_name
        self.dest_connection_name = self.params.dest_connection_name
        self.get_model_classes()
        self.get_resources()

        # self.database = get_databases_item_value(alias=self.params.source_connection_name)
        self.export_database_name = None

        self.resource = self._create_resource_instance()

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

        if self.source_connection_name:
            self.source_connection = self.get_connection_by_alias(self.source_connection_name)
        # if self.source_model:
        #     self._source_model._meta.model.objects.using(self.source_connection_name)

            # self.source_model._meta.model.objects._db = (
            #     self.source_connection_name
            # )

    # def source_model(self):
    #     source_model = self.get_source_model_class()
    #     if source_model:
    #         self.headers = self._get_exported_headers()
    #
    #     if self.source_connection_name:
    #         source_model._meta.model.objects.using(self.source_connection_name)
    #         # source_model._meta.model.objects._db = (
    #         #     self.source_connection_name
    #         # )
    #     return source_model

    @property
    def source_model(self):
        return self._source_model

    @source_model.setter
    def source_model(self, value):
        """Set property to the source model and define what connect we will be using farther"""
        self._source_model = value
        if self.source_model:
            self.headers = self._get_exported_headers()
        # if self.source_connection_name:
        #     self._source_model._meta.model.objects.using(self.source_connection_name)

    @property
    def dest_model(self):
        return self._dest_model

    @dest_model.setter
    def dest_model(self, value):
        self._dest_model = value
        # if self.dest_connection_name:
        #     self._dest_model._meta.model.objects.using(self.dest_connection_name)
        #     # self.dest_model._meta.model.objects._db = self.dest_connection_name

    @property
    def dest_connection_name(self):
        return self._dest_connection_name

    @dest_connection_name.setter
    def dest_connection_name(self, value: str):
        self._dest_connection_name = value

        if self.dest_connection_name:
            self.dest_connection = self.get_connection_by_alias(self.dest_connection_name)
        # if self.dest_model:
        #     self._dest_model._meta.model.objects.using(self.dest_connection_name)

    def restore_default(
        self,
        source_connection_name: str,
        source_table_name: str,
        dest_connection_name: str,
        dest_table_name: str
    ) -> None:

        self.source_connection_name = source_connection_name
        self.source_table_name = source_table_name
        self.dest_connection_name = dest_connection_name
        self.dest_table_name = dest_table_name

    def get_source_model_class(self):
        return self.get_model_class(
            self.source_model_module, "models", self.source_table_name
        )

    def get_dest_model_class(self):
        return self.get_model_class(
            self.dest_model_module, "models", self.dest_table_name
        )

    def get_model_classes(self):
        ###########################################################################
        # First setting connection and then attach using_db to source model
        ###########################################################################
        self.source_model = self.get_source_model_class()

        ###########################################################################
        # First setting connection and then attach using_db to destination model
        ###########################################################################
        self.dest_model = self.get_dest_model_class()

    def get_resources(self):
        self.resources = dict(
            self.get_list_classes(
                ETL.PIPE_MODULES.DBF_IMPORT
                if self.type == ETL.EXPORT.DBF
                else ETL.PIPE_MODULES.DOC2SQL_IMPORT,
                ETL.PIPE_MODULES.DBF_RESOURCE
                if self.type == ETL.EXPORT.DBF
                else ETL.PIPE_MODULES.DOC2SQL_RESOURCE,
                resources.ModelResource,
            )
        )

    def print(self, message: str) -> None:
        if self.logger:
            self.logger.info(message)
        else:
            print(message)

    def get_copy_params(self, params):
        return copy.copy(params)

    def _get_real_database_name(self):
        return settings.DATABASES[self.source_connection_name]["NAME"]

    def _get_real_localfts_name(self):
        return settings.DATABASES[ETL.CONNECT.LOCALFTS]["NAME"]

    def _get_real_source_table_name(self):
        return self.source_model._meta.db_table

    def _get_real_dest_table_name(self):
        return self.dest_model._meta.db_table

    def _get_resource_models(self) -> resources.ModelResource:
        for name, model in self.resources.items():
            if (
                model.Meta.model.__name__.lower()
                == self.dest_model._meta.model.__name__.lower()
            ):
                resource_model = model()
                return resource_model

    def _get_exported_headers(self) -> list:
        """Return fields list from model"""
        return [
            field.attname.lower() for field in self.source_model._meta.fields
        ]

    def _get_imported_headers(self) -> list:
        """Return fields list from model"""
        return [field.attname for field in self.dest_model._meta.fields]

    # def _get_source_database_id(self) -> str:
    #     """
    #     Extract dir from settings.DATABASES[][NAME]
    #     Return "NAME":str = "\\\\192.168.0.122\\BASES\\GTD_2022_LG"
    #
    #     :return: DBF data directory name
    #     """
    #     try:
    #         return get_databases_item_value(
    #             alias=self.source_connection_name, key="NAME"
    #         ).lower()
    #     except AttributeError:
    #         raise

    def _get_dest_database_id(self) -> str:
        """
        Extract dir from settings.DATABASES[][NAME]
        Return "NAME":str = "\\\\192.168.0.122\\BASES\\GTD_2022_LG"

        :return: DBF data directory name
        """
        try:
            return get_databases_item_value(
                alias=self.dest_connection_name, key="NAME"
            ).lower()
        except AttributeError:
            raise

    def _create_resource_instance(self):
        resource_model = self._get_resource_models()
        # Class property
        resource_model.type = self.type
        # Meta property
        # self.database = get_databases_item_value(alias=self.params.source_connection_name).lower()
        resource_model._meta.poll_pk = self.params.poll_pk
        resource_model._meta.using_db = self.params.dest_connection_name
        # resource_model._meta.database = get_databases_item_value(alias=resource_model._meta.using_db)
        resource_model._meta.redis_message_id = self._redis_message_id

        return resource_model

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
            self.logger.exception(e)
            raise e

    def get_list_classes(self, entry, module_name, base_class) -> list:

        try:
            app_module = import_module(entry)
        except Exception as e:
            self.logger.exception(e)
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
                    issubclass(candidate, base_class)
                    and candidate is not base_class
                    and hasattr(candidate, "type")
                )
            ]

        return res_models

    def _get_export_raw_sql(self) -> str:
        """Return raw sql for export model"""
        return self.source_model.__class__.objects.all().query.__str__()

    def get_list_tables_from_model_class(
        self, entry: str, module_name: str
    ) -> list:
        """Return list of table names selected in the db_table property Meta class"""
        return [
            klass._meta.db_table
            for _, klass in self.get_list_classes(
                entry, module_name, models.Model
            )
        ]

    def get_model_class(
        self, entry: str, module_name: str, db_table: str
    ) -> models:
        """Return model associated with the db_table property Meta class"""
        return [
            klass
            for _, klass in self.get_list_classes(
                entry, module_name, models.Model
            )
            if (klass._meta.db_table.lower() == db_table.lower())
        ][0]() or None

    def _delete_all_imported_records(self, model: models) -> int:
        # clearing down existing objects
        sql = f"TRUNCATE TABLE {model._meta.db_table}"
        result = self.execute_query(self.resource._meta.using_db, sql)
        return result.rowcount

    def dbf_record_count(self) -> int:
        """Calculate rows in DBF
        :rtype: object
        """
        sql = f"SELECT COUNT(*) as RECC FROM {self.source_model._meta.db_table};"
        rows = self._execute_query(sql)
        count = 0
        for row in rows:
            count = row[0]
        return count

    def _imported_field_exist(self, field: str):
        result = [
            field
            for f in self._get_imported_headers() if f.lower() == field.lower()
        ]
        return result or None

    def _exported_field_exist(self, field: str):
        result = [
            field
            for f in self._get_exported_headers() if f.lower() == field.lower()
        ]
        return result[0] or None

    def gomonth(self, today: datetime.date, month: int):
        return today + relativedelta(months=+month)

    def arm_record_count(self) -> int:
        """Calculate was exported rows"""
        field = self._exported_field_exist(ETL.FIELD.G072)

        today = datetime.date.today()
        last = self.gomonth(today=today, month=self._period_of_month)

        if field:
            result = self.source_model.__class__.objects.using(self.source_connection_name). \
                    filter(g072__gte=last, g072__lte=today).count()
        else:
            result = self.source_model.__class__.objects.using(self.source_connection_name).count()

        return result

    def execute_query(self, connection_name: str, row_sql: str, params=None):
        try:
            connection = self.get_connection_by_alias(connection_name)
            return connection.cursor().execute(row_sql, params)
        except Exception as e:
            self.logger.exception(e)
            raise e

    # def get_actual_arm_record(self, connection_name):
    #     self.source_connection = self.get_connection_by_alias(connection_name)
    #     sql = f"""
    #             SELECT
    #                 QUOTENAME(SCHEMA_NAME(sOBJ.schema_id)) + '.' + QUOTENAME(sOBJ.name) AS [table_name]
    #                 ,SUM(sPTN.Rows) AS [row_count]
    #             FROM [gtd_0_arm_2022_dbk1].[sys].[objects] AS sOBJ
    #                 INNER JOIN [gtd_0_arm_2022_dbk1].[sys].[partitions] AS sPTN
    #                 ON sOBJ.object_id = sPTN.object_id
    #             WHERE sOBJ.type = 'U'
    #               AND sOBJ.is_ms_shipped = 0x0
    #               AND index_id < 2 -- 0:Heap, 1:Clustered
    #             GROUP BY sOBJ.schema_id, sOBJ.name
    #             ORDER BY [table_name]
    #            """
    #     rows = self._execute_query(sql)
    #
    #     return rows
