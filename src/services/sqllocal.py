import logging
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

        # self._reccount = 0

    def start_import(self):
        """Process importing data from DBF to SQL Server"""
        try:
            delete_dbf_sql = self._delete_dbf_statement()
            delete_arm_sql = self._delete_arm_statement()
            insert_sql = self._insert_statement()
            sql = f"{delete_dbf_sql} {delete_arm_sql} {insert_sql}"
            with transaction.atomic(using=self.dest_connection_name):
                self.print(sql)
                # self._execute_query(sql)

        except Exception as e:
            logger.exception(e)
            raise e

    def _insert_statement(self):
        source_database_name = self._get_real_database_name()
        dest_database_name = self._get_real_localfts_name()
        table_name = self._get_real_source_table_name()
        fields = self._get_sql_fields_list()

        sql = (f"\n"
               f"INSERT INTO [{dest_database_name}].[dbo].[{table_name}] \n"
               f"    (\n"
               f"        {fields}\n"
               f"    )\n"
               f"    SELECT {fields} FROM [{source_database_name}].[dbo].[{table_name}]\n"
               f"        WHERE [{ETL.FIELD.HASH}] NOT IN (\n"
               f"            SELECT [{ETL.FIELD.HASH}] FROM [{dest_database_name}].[dbo].[{table_name}]\n"
               f"        )\n")
        # self.print(sql)
        return sql

    def _source_model_record_count(self):
        return self.source_model.__class__.objects.using(self.source_connection_name).count()


    def _delete_dbf_statement(self):
        # DELETE FROM [LocalFts].[dbo].[tdclhead]
        #   WHERE [hash] NOT IN (SELECT [hash] FROM [gtd_2022_smolensk].[dbo].[tdclhead])
        #     AND [sourcetype] = 'DBF' AND [database] = 'gtd_2022_smolensk'
        dest_database_name = self._get_real_localfts_name()
        source_database_name = self._get_real_database_name()
        table_name = self._get_real_source_table_name()
        sql = (f"\n"
               f"DELETE FROM [{dest_database_name}].[dbo].[{table_name}]\n"
               f"    WHERE [{ETL.FIELD.HASH}] NOT IN (\n"
               f"        SELECT [{ETL.FIELD.HASH}] FROM [{source_database_name}].[dbo].[{table_name}]\n"
               f"    )\n"
               f"        AND [{ETL.FIELD.EXPTYPE}] = '{self.type}' AND [{ETL.FIELD.DATABASE}] = '{self.database}'\n")
        # self.print(sql)
        return sql

    def _delete_arm_statement(self):
        dest_database_name = self._get_real_localfts_name()
        source_database_name = self._get_real_database_name()
        table_name = self._get_real_source_table_name()
        sql = (f"\n"
               f"DELETE FROM [{dest_database_name}].[dbo].[{table_name}]\n"
               f"    WHERE [{ETL.FIELD.G07X}] IN (\n"
               f"        SELECT [{ETL.FIELD.G07X}] FROM [{source_database_name}].[dbo].[{table_name}]\n"
               f"            WHERE [{ETL.FIELD.HASH}] NOT IN  (\n"
               f"               SELECT [{ETL.FIELD.HASH}] FROM [{dest_database_name}].[dbo].[{table_name}]\n" 
               f"        )\n" 
               f"    )\n"
               f"    AND [{ETL.FIELD.EXPTYPE}] = '{ETL.EXPORT.DOC2SQL}'\n")
        # self.print(sql)
        return sql
