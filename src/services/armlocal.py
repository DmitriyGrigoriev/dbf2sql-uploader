from django.db import transaction
from src.services.base.baseimport import BaseImport
from src.apps.common.dataclasses import ETL


class ARMLocalFts(BaseImport):
    # params = ImportInfo.from_dict({'table_pk': 1922, 'poll_pk': 15, 'source_connection_name': 'arm_edh',
    # 'source_table_name': 'KTDTRANS', 'dest_connection_name': 'gtd_arm_test', 'dest_table_name': 'KTDTRANS',
    # 'data_directory': 'KTDTRANS', 'type': 'ARM', 'last_write': '2022-10-11T00:00:51.396724', 'upload_record': 39,
    # 'table_record': 0, 'status': 'failed', 'redis_message_id': '6b297627-5a9f-45bc-8a21-a4690e378e83'})
    def run_import(self) -> None:
        """Process importing data from DBF to SQL Server"""
        try:
            with transaction.atomic(using=self.dest_connection_name):
                # insert records to LocalFts
                sql = self._create_insert_statement()
                self._execute_query(sql)

        except Exception as e:
            if self.logger:
                self.logger.error(f"Error occurred while insert data from database "
                                  f"{self._get_real_database_name()} table {self._get_real_source_table_name()} "
                                  f"into {self._get_real_localfts_name()} table {self._get_real_dest_table_name()}"
                                  )
            raise e

    def _get_identical_fields(self) -> str:
        source_fields_set = {
            f.name.lower() for f in self.source_model._meta.fields if f.name != self.source_model._meta.pk.name
        }

        dest_fields_set = {
            f.name for f in self.dest_model._meta.fields if f.name != self.dest_model._meta.pk.name
        }
        # get fields if they only exist in specific LocalFts table
        fields_set = dest_fields_set.intersection(source_fields_set)
        fields = ""
        for f in fields_set:
            fields += f"[{f}], "
        # remove 2 last symbols
        result = fields[0:-2]
        return result

    def _create_insert_statement(self) -> str:
        source_database_name: str = self._get_real_database_name()
        source_table_name: str = self._get_real_source_table_name()
        dest_database_name: str = self._get_real_localfts_name()
        dest_table_name: str = self._get_real_dest_table_name()
        fields: str = self._get_identical_fields()
        sql: str = \
            (f"\n"
             f"INSERT INTO [{dest_database_name}].[dbo].[{dest_table_name}] \n"
             f"    (\n"
             f"        {fields}\n"
             f"    )\n"
             f"    SELECT {fields} FROM [{source_database_name}].[dbo].[{source_table_name}]\n"
             f"        WHERE [{ETL.FIELD.G07X}] NOT IN (SELECT [{ETL.FIELD.G07X}] FROM [{dest_database_name}].[dbo].[{dest_table_name}])\n")

        return sql
