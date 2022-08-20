import logging
from django.db import models
from src.services.base.baseimport import BaseImport
from src.config import settings

logger = logging.getLogger(__name__)


class SQLLocalFts(BaseImport):
    delete_imported_records = True
    _source_connection_name = None
    _dest_connection_name = None
    _source_model = None
    _dest_model = None


    def __init__(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str, logger=None
                 ) -> None:
        self.source_table_name = source_table_name
        self.dest_table_name = dest_table_name

        self.source_model = self.get_model_class(settings.IMPORT_MODULE, 'models', self.dest_table_name)
        self.source_connection_name = dest_connection_name

        self.dest_model = self.get_model_class(settings.IMPORT_MODULE, 'models', self.dest_table_name)
        self.dest_connection_name = settings.CONNECTION_FTS

        self.database = self._get_source_database_id()


    def start_import(self):
        """Process importing data from DBF to SQL Server"""
        try:
            self._delete_mark_database_records(model=self.dest_model)
            sql = self._create_insert_sql()
            self._execute_query(sql)

        except Exception as e:
            logger.exception(e)
            raise e

        return True


    # setter
    def set_source_connection_name(self, value):
        self._source_connection_name = value
        if self.source_model:
            self.source_model._meta.model.objects._db = self._source_connection_name

        self.source_connection = self.get_connection_by_alias(self.source_connection_name)


    #getter
    def get_source_connection_name(self):
        return self._source_connection_name

    source_connection_name = property(get_source_connection_name, set_source_connection_name)

    # setter
    def set_dest_connection_name(self, value: str):
        self._dest_connection_name = value
        if self.dest_model:
            self.dest_model._meta.model.objects._db = self._dest_connection_name

        self.dest_connection = self.get_connection_by_alias(self.dest_connection_name)

    #getter
    def get_dest_connection_name(self):
        return self._dest_connection_name

    dest_connection_name = property(get_dest_connection_name, set_dest_connection_name)


    def _execute_query(self, row_sql: str)-> list:
        """Return rows by executing query SELECT * from dbf_model"""
        #self.source_connection
        return self.source_connection.cursor().execute(row_sql)


    def _create_insert_sql(self):
        fields_set = [f.name for f in self.source_model._meta.fields if f.name != self.source_model._meta.pk.name]
        dest_database_name = settings.DATABASES[settings.CONNECTION_FTS]["NAME"]
        source_database_name = settings.DATABASES[self.source_connection_name]['NAME']
        table_name = self.source_model._meta.db_table
        insert = f"INSERT INTO [{dest_database_name}].[dbo].[{table_name}] "
        fields = ""
        for f in fields_set:
            fields += f"[{f}], "
        # remove 2 last symbols
        result = fields[0:-2]

        sql = f"{insert} ({result}) SELECT {result} FROM [{source_database_name}].[dbo].[{table_name}]"

        return sql


    def _delete_mark_database_records(self, model: models) -> bool:
        """
        Delete record where src field equal source DBF data directory name

        :param model: Destination model (MSSQL Server table)
        :return: True
        """
        # Delete all table records where field src=self.database
        try:
            model.__class__.objects.using(self.dest_connection.alias).filter(database=self.database).delete()
        except Exception as e:
            logger.exception(e)
            raise e

        return True


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



