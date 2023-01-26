# import logging
from django.db import transaction
from src.apps.common.dataclasses import ETL, ImportInfo
from src.services.base.baseimport import BaseImport, get_databases_item_value

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
        self.params = self.get_export_params(self.get_copy_params(params))
        self.partial = is_partial
        self.export_database_name = get_databases_item_value(alias=self.params.source_connection_name)

    def run_import(self):
        """Process importing data from DBF to SQL Server"""
        try:
            if not hasattr(self.dest_model, 'unique_hash'):
                raise AttributeError("'source_model' object has no attribute 'unique_hash'")

            connection_name = self.params.dest_connection_name

            if not self.partial:
                if self.dest_model.unique_hash:
                    delete_dbf_sql = self.delete_dbf_statement_by_hash()
                if not self.dest_model.unique_hash:
                    delete_dbf_sql = self.delete_dbf_statement()
                # Run each sql as an isolate transaction to avoid deadlock error: 40001
                with transaction.atomic(using=connection_name, savepoint=False):
                    self.execute_query(connection_name=connection_name, row_sql=delete_dbf_sql)

                with transaction.atomic(using=connection_name, savepoint=False):
                    delete_arm_sql = self.delete_arm_statement()
                    self.execute_query(connection_name=connection_name, row_sql=delete_arm_sql)

            with transaction.atomic(using=connection_name, savepoint=False):
                insert_sql = self.insert_statement()
                self.execute_query(connection_name=connection_name, row_sql=insert_sql)

            return self.local_fts_records_count()

        except Exception as e:
            self.logger.exception(e)
            raise e

    def get_export_params(self, p: ImportInfo):
        params: ImportInfo = p
        params.source_connection_name = p.dest_connection_name
        params.source_table_name = p.dest_table_name
        params.dest_connection_name = ETL.CONNECT.LOCALFTS
        return params

    def insert_statement(self):
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
        database_name = get_databases_item_value(self.dest_connection_name)
        local_fts = self._get_real_localfts_name()
        table_name = self.params.source_table_name.lower()
        fields = self._get_sql_fields_list()

        sql = (f"\n"
               f"INSERT INTO [{local_fts}].[dbo].[{table_name}] \n"
               f"    (\n"
               f"        {fields}\n"
               f"    )\n"
               f"    SELECT {fields} FROM [{database_name}].[dbo].[{table_name}]\n"
               f"        WHERE [{ETL.FIELD.HASH}] NOT IN (\n"
               f"            SELECT [{ETL.FIELD.HASH}] FROM [{local_fts}].[dbo].[{table_name}]\n"
               f"        )\n"
               f"    AND g07x NOT IN (\n"
               f"    	SELECT l.[{ETL.FIELD.G07X}] \n"
               f"    		FROM [{local_fts}].[dbo].[{table_name}] l \n"
               f"		    INNER JOIN [{database_name}].[dbo].[{table_name}] t \n"
               f"			ON l.[{ETL.FIELD.G07X}] = t.[{ETL.FIELD.G07X}] \n"
               f"		WHERE l.[{ETL.FIELD.DATABASE}] NOT IN ('{self.export_database_name.lower()}') \n"
               f"		GROUP BY l.[{ETL.FIELD.G07X}], l.[{ETL.FIELD.DATABASE}] \n"
               f"    )\n")

        self.print(f"\n################## Insert statement for {table_name.upper()}  "
                   f"##################: {sql}")
        return sql

    def _get_sql_fields_list(self) -> str:
        fields_set = [
            f.name
            for f in self.dest_model._meta.fields
            if f.name != self.dest_model._meta.pk.name
        ]
        fields = ""
        for f in fields_set:
            fields += f"[{f}], "
        # remove 2 last symbols
        result = fields[0:-2]
        return result

    def local_fts_records_count(self):
        return self.dest_model.__class__.objects.using(self.params.dest_connection_name).\
            filter(sourcetype=ETL.EXPORT.DBF, database=self.export_database_name).count()

    def delete_dbf_statement(self):
        # DELETE FROM [LocalFts].[dbo].[tdclhead]
        #   WHERE [sourcetype] = 'DBF' AND [database] = 'gtd_2022_smolensk'
        local_fts = self._get_real_localfts_name()
        table_name = self.params.source_table_name.lower()
        sql = (f"\n"
               f"DELETE [{table_name}] FROM [{local_fts}].[dbo].[{table_name}]\n"
               f"    WHERE [{ETL.FIELD.EXPTYPE}] = '{self.type}' AND [{ETL.FIELD.DATABASE}] = '{self.export_database_name.lower()}'\n")

        self.print(f"\n################## Delete type {ETL.EXPORT.DBF} records "
                   f"in {table_name.upper()}  ##################: {sql}")
        return sql

    def delete_dbf_statement_by_hash(self):
        # DELETE FROM [LocalFts].[dbo].[tdclhead]
        #   WHERE [hash] NOT IN (SELECT [hash] FROM [gtd_2022_smolensk].[dbo].[tdclhead])
        #     AND [sourcetype] = 'DBF' AND [database] = 'gtd_2022_smolensk'
        local_fts = self._get_real_localfts_name()
        database_name = get_databases_item_value(self.params.source_connection_name)
        table_name = self.params.source_table_name.lower()
        source_database = get_databases_item_value(alias=self.resource._meta.using_db)
        sql = (f"\n"
               f"DELETE [{table_name}] FROM [{local_fts}].[dbo].[{table_name}]\n"
               f"    WHERE [{ETL.FIELD.HASH}] NOT IN (\n"
               f"        SELECT [{ETL.FIELD.HASH}] FROM [{database_name}].[dbo].[{table_name}]\n"
               f"    )\n"
               f"      AND [{ETL.FIELD.EXPTYPE}] = '{self.type}'\n"
               f"      AND [{ETL.FIELD.DATABASE}] = '{source_database.lower()}'\n")

        self.print(f"\n################## Delete type {ETL.EXPORT.DBF} records "
                   f"by unique {ETL.FIELD.HASH} in {table_name.upper()} ##################:"
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
        local_fts = self._get_real_localfts_name()
        database_name = get_databases_item_value(self.params.source_connection_name)
        table_name = self.params.source_table_name.lower()
        sql = (f"\n"
               f"DELETE [{table_name}] FROM [{local_fts}].[dbo].[{table_name}]\n"
               f"    INNER JOIN (\n"
               f"        SELECT [{ETL.FIELD.G07X}] FROM [{database_name}].[dbo].[{table_name}]\n"
               f"            WHERE [{ETL.FIELD.HASH}] NOT IN  (\n"
               f"               SELECT [{ETL.FIELD.HASH}] FROM [{local_fts}].[dbo].[{table_name}]\n" 
               f"        )\n" 
               f"    ) AS T ON [{table_name}].[{ETL.FIELD.G07X}] = T.[{ETL.FIELD.G07X}]\n"
               f"    WHERE [{ETL.FIELD.EXPTYPE}] = '{ETL.EXPORT.DOC2SQL}'\n")

        self.print(f"\n################## Delete type {ETL.EXPORT.DOC2SQL} "
                   f"records in {table_name.upper()} ##################: {sql}")
        return sql
