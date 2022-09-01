import logging
from django.db import models
from django.db import transaction
from src.services.base.baseimport import BaseImport
from src.config import settings

logger = logging.getLogger(__name__)


class SQLLocalFts(BaseImport):
    _type = 'DBF'

    def __init__(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str, logger=None
                 ) -> None:
        ######################################################################
        # Second step: GTD_2022_SMOLENSK.dbo.TDCLHEAD -> LocalFts.dbo.TDCLHEAD
        # SQLLocalFts(
        #     source_connection_name='gtd_2022_smolensk',
        #     source_table_name='TDCLHEAD',
        #     dest_connection_name='localfts',
        #     dest_table_name='TDCLHEAD',
        #     logger=None
        # ).start_import()
        #######################################################################
        self.source_table_name = source_table_name
        self.dest_table_name = dest_table_name

        self.source_model = self.get_model_class(
            settings.PIPE_MODULES[self._type]['import'], 'models', self.source_table_name
        )
        self.source_connection_name = source_connection_name

        self.dest_model = self.get_model_class(
            settings.PIPE_MODULES[self._type]['import'], 'models', self.dest_table_name
        )
        self.dest_connection_name = dest_connection_name

        self.database = self._get_source_database_id()


    def start_import(self):
        """Process importing data from DBF to SQL Server"""
        try:
            # self._delete_mark_database_records(model=self.dest_model)
            with transaction.atomic(using=self.dest_connection_name):
                # delete records step 1
                sql = self._delete_dbf_statement()
                self._execute_query(sql)
                # delete records step 2
                sql = self._delete_arm_statement()
                self._execute_query(sql)
                # insert records step 3
                sql = self._create_insert_statement()
                self._execute_query(sql)

        except Exception as e:
            logger.exception(e)
            raise e


    def _create_insert_statement(self):
        dest_database_name = self._get_real_localfts_name()
        source_database_name = self._get_real_database_name()
        table_name = self._get_real_source_table_name()
        insert = f"INSERT INTO [{dest_database_name}].[dbo].[{table_name}] "
        where = f" WHERE [g07x] NOT IN (SELECT [g07x] FROM [{dest_database_name}].[dbo].[{table_name}])"
        fields = self._get_sql_fields_list()

        sql = f"{insert} ({fields}) SELECT {fields} FROM [{source_database_name}].[dbo].[{table_name}] {where}"

        return sql


    def _delete_dbf_statement(self):
        # DELETE FROM [LocalFts].[dbo].[tdclhead]
        #   WHERE [hash] NOT IN (SELECT [hash] FROM [gtd_2022_smolensk].[dbo].[tdclhead])
        #     AND [sourcetype] = 'DBF'
        dest_database_name = self._get_real_localfts_name()
        source_database_name = self._get_real_database_name()
        table_name = self._get_real_source_table_name()
        where = f" WHERE [hash] NOT IN (SELECT [hash] FROM [{source_database_name}].[dbo].[{table_name}])" \
                f" AND [sourcetype] = '{self._type}'"

        sql = f"DELETE FROM [{dest_database_name}].[dbo].[{table_name}] {where}"

        return sql


    def _delete_arm_statement(self):
        # DELETE FROM [LocalFts].[dbo].[tdclhead]
        #   WHERE [g07x] NOT IN (SELECT [g07x] FROM [gtd_2022_smolensk].[dbo].[tdclhead])
        #     AND [sourcetype] = 'ARM'
        dest_database_name = self._get_real_localfts_name()
        source_database_name = self._get_real_database_name()
        table_name = self._get_real_source_table_name()
        where = f" WHERE [g07x] IN (SELECT [g07x] FROM [{source_database_name}].[dbo].[{table_name}])" \
                f" AND [sourcetype] = 'ARM'"

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



