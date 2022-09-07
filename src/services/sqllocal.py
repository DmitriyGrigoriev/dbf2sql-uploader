import logging
from django.db import models
from django.db import transaction
from src.services.base.baseimport import BaseImport
from src.apps.common.dataclasses import ETL

logger = logging.getLogger(__name__)


class SQLLocalFts(BaseImport):

    def __init__(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str,
                 export_database_name: str,
                 logger=None, mode: str = ETL.MODE.FULL
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
        # super(SQLLocalFts, self).__init__(
        #     source_connection_name,
        #     source_table_name,
        #     dest_connection_name,
        #     dest_table_name,
        #     logger,
        #     mode
        # )
        #######################################################################
        super(SQLLocalFts, self).__init__()

        self.type = ETL.EXPORT.DBF
        self.source_model_module = ETL.PIPE_MODULES.DBF_IMPORT
        self.dest_model_module = ETL.PIPE_MODULES.DBF_IMPORT

        self.source_connection_name = source_connection_name
        self.dest_connection_name = dest_connection_name

        self.source_table_name = source_table_name
        self.dest_table_name = dest_table_name

        self.export_database_name = export_database_name

        self.logger = logger
        self.mode = mode

        self.get_model_classes()
        self.get_resources()

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
                sql = self._insert_statement()
                self._execute_query(sql)

        except Exception as e:
            logger.exception(e)
            raise e


    def _insert_statement(self):
        source_database_name = self._get_real_database_name()
        dest_database_name = self._get_real_localfts_name()
        table_name = self._get_real_source_table_name()
        fields = self._get_sql_fields_list()

        sql = f"""
               INSERT INTO [{dest_database_name}].[dbo].[{table_name}] 
                    (
                        {fields}
                    )
                    SELECT {fields} FROM [{source_database_name}].[dbo].[{table_name}]
                        WHERE [{ETL.FIELD.HASH}] NOT IN (
                            SELECT [{ETL.FIELD.HASH}] FROM [{dest_database_name}].[dbo].[{table_name}]
                                WHERE [{ETL.FIELD.EXPTYPE}] = '{self.type}' 
                                  AND [{ETL.FIELD.DATABASE}] = '{self.export_database_name}') 
               """
        # self.print(sql)
        return sql


    def _delete_dbf_statement(self):
        # DELETE FROM [LocalFts].[dbo].[tdclhead]
        #   WHERE [hash] NOT IN (SELECT [hash] FROM [gtd_2022_smolensk].[dbo].[tdclhead])
        #     AND [sourcetype] = 'DBF' AND [database] = 'gtd_2022_smolensk'
        dest_database_name = self._get_real_localfts_name()
        source_database_name = self._get_real_database_name()
        table_name = self._get_real_source_table_name()

        sql = f"""
               DELETE FROM [{dest_database_name}].[dbo].[{table_name}]
                    WHERE [{ETL.FIELD.HASH}] NOT IN (
                        SELECT [{ETL.FIELD.HASH}] FROM [{source_database_name}].[dbo].[{table_name}]
                    )
                      AND [{ETL.FIELD.EXPTYPE}] = '{self.type}' AND [{ETL.FIELD.DATABASE}] = '{self.database}'
               """
        # self.print(sql)
        return sql


    def _delete_arm_statement(self):
        # DELETE FROM [LocalFts].[dbo].[tdclhead]
        #   WHERE [g07x] NOT IN (SELECT [g07x] FROM [gtd_2022_smolensk].[dbo].[tdclhead])
        #     AND [sourcetype] = 'ARM' AND [database] = 'gtd_2022_smolensk'
        dest_database_name = self._get_real_localfts_name()
        source_database_name = self._get_real_database_name()
        table_name = self._get_real_source_table_name()

        sql = f"""
               DELETE FROM [{dest_database_name}].[dbo].[{table_name}]
                    WHERE [{ETL.FIELD.G07X}] NOT IN (
                        SELECT [{ETL.FIELD.G07X}] FROM [{source_database_name}].[dbo].[{table_name}]
                    )
                AND [{ETL.FIELD.EXPTYPE}] = '{ETL.EXPORT.DOC2SQL}'
                
               DELETE FROM [{dest_database_name}].[dbo].[{table_name}] 
                    WHERE [{ETL.FIELD.G07X}] IN (
                        SELECT [{ETL.FIELD.G07X}] FROM [{source_database_name}].[dbo].[{table_name}]
                            WHERE [{ETL.FIELD.EXPTYPE}] = '{self.type}'
                    )
                AND [{ETL.FIELD.EXPTYPE}] = '{ETL.EXPORT.DOC2SQL}'
               """
        # self.print(sql)
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



