# import logging
from django.db import transaction
from src.services.base.baseimport import BaseImport
from src.apps.common.dataclasses import ETL

# logger = logging.getLogger(__name__)


class SQLLocalFts(BaseImport):

    def __init__(self, params, is_partial: bool = False) -> None:
        ######################################################################
        # Second step: GTD_2022_SMOLENSK.dbo.TDCLHEAD -> LocalFts.dbo.TDCLHEAD
        # SQLLocalFts(
        #     source_connection_name='gtd_2022_smolensk',
        #     source_table_name='TDCLHEAD',
        #     dest_connection_name='localfts',
        #     dest_table_name='TDCLHEAD',
        #     logger=None
        # ).run_import()
        #######################################################################
        super(SQLLocalFts, self).__init__(params)
        self.partial = is_partial
        self.export_database_name = self._get_source_database_id()

    def run_import(self):
        """Process importing data from DBF to SQL Server"""
        try:
            if not hasattr(self.source_model, 'unique_hash'):
                raise AttributeError("'source_model' object has no attribute 'unique_hash'")

            if not self.partial:
                if self.source_model.unique_hash:
                    delete_dbf_sql = self.delete_dbf_statement_by_hash()
                if not self.source_model.unique_hash:
                    delete_dbf_sql = self.delete_dbf_statement()
                # Run each sql as an isolate transaction to avoid deadlock error: 40001
                with transaction.atomic(using=self.dest_connection_name, savepoint=False):
                    self._execute_query(delete_dbf_sql)

                with transaction.atomic(using=self.dest_connection_name, savepoint=False):
                    delete_arm_sql = self.delete_arm_statement()
                    self._execute_query(delete_arm_sql)

            with transaction.atomic(using=self.dest_connection_name, savepoint=False):
                insert_sql = self.insert_statement()
                self._execute_query(insert_sql)

            return self._dest_model_record_count()

        except Exception as e:
            self.logger.exception(e)
            raise e

    def insert_statement(self):
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

        self.print(f"\n################## Insert statement for {self._get_real_source_table_name().upper()}  "
                   f"##################: {sql}")
        return sql

    def _source_model_record_count(self):
        # SELECT COUNT(*) FROM [LocalFts].[dbo].[tdclhead]
        #   WHERE [sourcetype] = 'DBF' AND [database] = 'gtd_2022_smolensk'
        return self.source_model.__class__.objects.using(self.source_connection_name).count()

    def _dest_model_record_count(self):
        return self.dest_model.__class__.objects.using(self.dest_connection_name).\
            filter(sourcetype=ETL.EXPORT.DBF, database=self.export_database_name).count()

    def delete_dbf_statement(self):
        # DELETE FROM [LocalFts].[dbo].[tdclhead]
        #   WHERE [sourcetype] = 'DBF' AND [database] = 'gtd_2022_smolensk'
        dest_database_name = self._get_real_localfts_name()
        table_name = self._get_real_source_table_name()
        sql = (f"\n"
               f"DELETE [{table_name}] FROM [{dest_database_name}].[dbo].[{table_name}]\n"
               f"    WHERE [{ETL.FIELD.EXPTYPE}] = '{self.type}' AND [{ETL.FIELD.DATABASE}] = '{self.export_database_name}'\n")

        self.print(f"\n################## Delete type {ETL.EXPORT.DBF} records "
                   f"in {self._get_real_source_table_name().upper()}  ##################: {sql}")
        return sql

    # def delete_partial_dbf_statement(self):
    #     # DELETE [tdcltechd] FROM [LocalFts].[dbo].[tdcltechd] l
    #     # 	INNER JOIN [gtd_2022_lg].[dbo].[tdcltechd] d
    #     # 		ON d.[hash] = l.[hash] AND d.[g07x] = l.[g07x]
    #     # WHERE l.[sourcetype] = 'DBF' AND l.[database] = 'gtd_2022_lg'
    #     dest_database_name = self._get_real_localfts_name()
    #     source_database_name = self._get_real_database_name()
    #     table_name = self._get_real_source_table_name()
    #     sql = (f"\n"
    #            f"DELETE [{table_name}] FROM [{source_database_name}].[dbo].[{table_name}] d\n"
    #            f"   INNER JOIN [{dest_database_name}].[dbo].[{table_name}] l\n"
    #            f"       ON d.[{ETL.FIELD.HASH}] = l.[{ETL.FIELD.HASH}] AND d.[{ETL.FIELD.G07X}] = l.[{ETL.FIELD.G07X}]\n"
    #            f"    WHERE l.[{ETL.FIELD.EXPTYPE}] = '{self.type}' AND [{ETL.FIELD.DATABASE}] = '{self.export_database_name}'\n")
    #     # self.print(sql)
    #     return sql


    def delete_dbf_statement_by_hash(self):
        # DELETE FROM [LocalFts].[dbo].[tdclhead]
        #   WHERE [hash] NOT IN (SELECT [hash] FROM [gtd_2022_smolensk].[dbo].[tdclhead])
        #     AND [sourcetype] = 'DBF' AND [database] = 'gtd_2022_smolensk'
        dest_database_name = self._get_real_localfts_name()
        source_database_name = self._get_real_database_name()
        table_name = self._get_real_source_table_name()
        sql = (f"\n"
               f"DELETE [{table_name}] FROM [{dest_database_name}].[dbo].[{table_name}]\n"
               f"    WHERE [{ETL.FIELD.HASH}] NOT IN (\n"
               f"        SELECT [{ETL.FIELD.HASH}] FROM [{source_database_name}].[dbo].[{table_name}]\n"
               f"    )\n"
               f"      AND [{ETL.FIELD.EXPTYPE}] = '{self.type}'\n"
               f"      AND [{ETL.FIELD.DATABASE}] = '{self.database}'\n")

        self.print(f"\n################## Delete type {ETL.EXPORT.DBF} records "
                   f"by unique {ETL.FIELD.HASH} in {self._get_real_source_table_name().upper()} ##################:"
                   f"{sql}")
        return sql

    def delete_arm_statement(self):
        # DELETE [tdcltechd] FROM [LocalFts].[dbo].[tdcltechd]
        #     INNER JOIN (
        #         SELECT [g07x] FROM [gtd_2022_lg].[dbo].[tdcltechd]
        #             WHERE [hash] NOT IN  (
        #                SELECT [hash] FROM [LocalFts].[dbo].[tdcltechd]
        #         )
        #     ) AS T ON [tdcltechd].[g07x] = T.[g07x]
        #     WHERE [sourcetype] = 'ARM'
        dest_database_name = self._get_real_localfts_name()
        source_database_name = self._get_real_database_name()
        table_name = self._get_real_source_table_name()
        sql = (f"\n"
               f"DELETE [{table_name}] FROM [{dest_database_name}].[dbo].[{table_name}]\n"
               f"    INNER JOIN (\n"
               f"        SELECT [{ETL.FIELD.G07X}] FROM [{source_database_name}].[dbo].[{table_name}]\n"
               f"            WHERE [{ETL.FIELD.HASH}] NOT IN  (\n"
               f"               SELECT [{ETL.FIELD.HASH}] FROM [{dest_database_name}].[dbo].[{table_name}]\n" 
               f"        )\n" 
               f"    ) AS T ON [{table_name}].[{ETL.FIELD.G07X}] = T.[{ETL.FIELD.G07X}]\n"
               f"    WHERE [{ETL.FIELD.EXPTYPE}] = '{ETL.EXPORT.DOC2SQL}'\n")

        self.print(f"\n################## Delete type {ETL.EXPORT.DOC2SQL} "
                   f"records in {self._get_real_source_table_name().upper()} ##################: {sql}")
        return sql
