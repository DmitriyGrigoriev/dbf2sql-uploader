import logging
# from django.db import models
from django.db import transaction
from src.services.base.baseimport import BaseImport
from src.config import settings

logger = logging.getLogger(__name__)


class ARMLocalFts(BaseImport):
    _type = 'ARM'

    def __init__(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str, logger=None
                 ) -> None:
        self.source_table_name = source_table_name
        self.dest_table_name = dest_table_name

        self.source_model = self.get_model_class(
            settings.PIPE_MODULES[self._type]['import'], 'models', self.dest_table_name[1:] # remove prefix
        )
        self.source_connection_name = source_connection_name

        self.dest_model = self.get_model_class(
            settings.PIPE_MODULES['DBF']['import'], 'models', self.dest_table_name
        )
        self.dest_connection_name = settings.CONNECTION_FTS

        self.database = self._get_source_database_id()

        self.logger = logger or None


    def start_import(self) -> None:
        """Process importing data from DBF to SQL Server"""
        try:
            # self._delete_mark_database_records(model=self.dest_model)
            with transaction.atomic(using=self.dest_connection_name):
                # delete records
                # sql = self._create_delete_statement()
                # self._execute_query(sql)
                # insert records
                sql = self._create_insert_statement()
                self._execute_query(sql)

        except Exception as e:
            if self.logger:
                source_database_name = self._get_real_database_name()
                source_table_name = self._get_real_source_table_name()
                dest_database_name = self._get_real_localfts_name()
                dest_table_name = self._get_real_dest_table_name()
                self.logger.error(f"Error occured while insert data from database "
                                  f"{source_database_name} table {source_table_name} "
                                  f"into {dest_database_name} table {dest_table_name}"
                                  )

            logger.exception(e)
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


    def _create_insert_statement(self):
        source_database_name = self._get_real_database_name()
        source_table_name = self._get_real_source_table_name()
        dest_database_name = self._get_real_localfts_name()
        dest_table_name = self._get_real_dest_table_name()
        insert = f"INSERT INTO [{dest_database_name}].[dbo].[{dest_table_name}] "
        where = f" WHERE [g07x] NOT IN (SELECT [g07x] FROM [{dest_database_name}].[dbo].[{dest_table_name}])"
        fields = self._get_identical_fields()

        sql = f"{insert} ({fields}) SELECT {fields} FROM [{source_database_name}].[dbo].[{source_table_name}] {where}"

        return sql
