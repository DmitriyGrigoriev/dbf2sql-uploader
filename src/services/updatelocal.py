import logging
from django.db import models
from src.services.base.baseimport import BaseImport
from src.config import settings

logger = logging.getLogger(__name__)


class SQLLocalFts(BaseImport):
    delete_imported_records = True
    # _source_connection_name = None
    # _dest_connection_name = None
    # _source_model = None
    # _dest_model = None


    def __init__(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str, logger=None
                 ) -> None:
        self.source_table_name = source_table_name
        self.dest_table_name = dest_table_name

        self.source_model = self.get_model_class(
            settings.PIPE_MODULES['DBF']['import'], 'models', self.dest_table_name
        )
        self.source_connection_name = dest_connection_name

        self.dest_model = self.get_model_class(
            settings.PIPE_MODULES['DBF']['import'], 'models', self.dest_table_name
        )
        self.dest_connection_name = settings.CONNECTION_FTS

        self.database = self._get_source_database_id()


    def start_import(self):
        """Process importing data from DBF to SQL Server"""
        try:
            self._delete_mark_database_records(model=self.dest_model)
            # delete records
            sql = self._create_delete_statement()
            self._execute_query(sql)
            # insert records
            sql = self._create_insert_statement()
            self._execute_query(sql)

        except Exception as e:
            logger.exception(e)
            raise e

        return True


    def _get_sql_fields_list(self)-> str:
        fields_set = [f.name for f in self.source_model._meta.fields if f.name != self.source_model._meta.pk.name]
        fields = ""
        for f in fields_set:
            fields += f"[{f}], "
        # remove 2 last symbols
        result = fields[0:-2]
        return result


    def _create_insert_statement(self):
        dest_database_name = self._get_real_localfts_name()
        source_database_name = self._get_real_database_name()
        table_name = self._get_real_table_name()
        insert = f"INSERT INTO [{dest_database_name}].[dbo].[{table_name}] "
        where = f" WHERE [hash] NOT IN (SELECT [hash] FROM [{dest_database_name}].[dbo].[{table_name}])"
        fields = self._get_sql_fields_list()

        sql = f"{insert} ({fields}) SELECT {fields} FROM [{source_database_name}].[dbo].[{table_name}] {where}"

        return sql


    def _create_delete_statement(self):
        dest_database_name = self._get_real_localfts_name()
        source_database_name = self._get_real_database_name()
        table_name = self._get_real_table_name()
        where = f" WHERE [hash] NOT IN (SELECT [hash] FROM [{source_database_name}].[dbo].[{table_name}])"

        sql = f"DELETE FROM [{dest_database_name}].[dbo].[{table_name}] {where}"

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



