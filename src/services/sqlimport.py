import tablib
import logging
from django.apps import apps
#from import_export import resources
from src.services.base.baseimport import BaseImport
from src.services.sqllocal import SQLLocalFts
from src.apps.common.dataclasses import ETL


logger = logging.getLogger(__name__)


def datetime_as_string(value):
    return value.strftime("%m/%d/%Y, %H:%M:%S")
    # ref: https://github.com/mkleehammer/pyodbc/issues/134#issuecomment-281739794
    # tup = struct.unpack("<6hI2h", dto_value)  # e.g., (2017, 3, 16, 10, 35, 18, 500000000, -6, 0)
    # return datetime(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5], tup[6] // 1000,
    #                 timezone(timedelta(hours=tup[7], minutes=tup[8])))


class SQLImport(BaseImport):

    def __init__(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str, logger=None,
                 mode: str = ETL.MODE.FULL
                 ) -> None:

        super(SQLImport, self).__init__()

        self.type = ETL.EXPORT.DBF
        self.source_model_module = ETL.PIPE_MODULES.DBF_EXPORT
        self.dest_model_module = ETL.PIPE_MODULES.DBF_IMPORT

        self.source_connection_name = source_connection_name
        self.dest_connection_name = dest_connection_name

        self.source_table_name = source_table_name
        self.dest_table_name = dest_table_name

        self.logger = logger
        self.mode = mode

        self.get_model_classes()
        self.get_resources()

    def start_import(self):
        """Process importing data from DBF to SQL Server"""
        ##########################################################################
        # First step: GTD_2022_SMOLENSK.DCLHEAD.DBF -> GTD_2022_SMOLENSK.TDCLHEAD
        # SQLImport(
        #     source_connection_name='dbf_2022_smolensk'
        #     source_table_name='DCLHEAD',
        #     dest_connection_name='gtd_2022_smolensk',
        #     dest_table_name='TDCLHEAD',
        #     logger=None
        # ).start_import()
        ##########################################################################
        try:
            if self.mode == ETL.MODE.FULL or self.mode == ETL.MODE.IMPORT:

                self.delete()
                self._reccount = self._source_model_record_count()
                raw_sql = self._get_export_raw_sql()

                resource = self._create_resource_instance()

                for start in range(0, self._reccount, self._limit):
                    # select data from dbf model
                    sql = self._transform_raw_select(start=start + 1, raw_sql=raw_sql)

                    if self.logger:
                        self.logger.info(f"Execute SQL: {sql}")

                    rows = self._execute_query(sql)
                    dataset = tablib.Dataset(headers=self.headers)

                    for row in rows:
                        dataset.append(row=row)

                    resource.import_data(dataset, use_transactions=False)
                    dataset.wipe()

            if self.mode == ETL.MODE.FULL or self.mode == ETL.MODE.EXPORT:
                # Update LocalFts
                self._reccount = self.after_import(
                    source_connection_name=self.source_connection_name,
                    source_table_name=self.source_table_name,
                    dest_connection_name=self.dest_connection_name,
                    dest_table_name=self.dest_table_name,
                    logger=self.logger,
                    mode=self.mode
                )

        except Exception as e:
            logger.info(f'Error occured in NAME[{self.dest_connection_name}] table {self.dest_table_name}')
            logger.exception(e)
            raise e

        return self._reccount

    def after_import(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str, logger=logger,
                 mode: str = ETL.MODE.FULL
                 ) -> int:
        ######################################################################
        # First step: GTD_2022_SMOLENSK.DCLHEAD.DBF -> GTD_2022_SMOLENSK.TDCLHEAD
        # SQLImport(
        #     source_connection_name='dbf_2022_smolensk'
        #     source_table_name='DCLHEAD',
        #     dest_connection_name='gtd_2022_smolensk',
        #     dest_table_name='TDCLHEAD',
        #     logger=None
        # ).start_import()
        ######################################################################
        # Second step: GTD_2022_SMOLENSK.dbo.TDCLHEAD -> LocalFts.dbo.TDCLHEAD
        # SQLLocalFts(
        #     source_connection_name='gtd_2022_smolensk',
        #     source_table_name='TDCLHEAD',
        #     dest_connection_name='localfts',
        #     dest_table_name='TDCLHEAD',
        #     export_database_name='gtd_2022_smolensk',
        #     logger=None
        # ).start_import()
        #######################################################################
        result = SQLLocalFts(
            source_connection_name=dest_connection_name,
            source_table_name=dest_table_name,
            dest_connection_name=ETL.CONNECT.LOCALFTS,
            dest_table_name=dest_table_name,
            export_database_name=self._get_source_database_id(),
            logger=logger,
            mode=mode
        ).start_import()

        # Restore using_db
        self.restore_default(
            source_connection_name, source_table_name,
            dest_connection_name, dest_table_name, logger=None,
            mode=mode
        )
        return result

    def _transform_raw_select(self, start: int, raw_sql: str) -> str:
        """Transform SQL expr [SELECT field1, fiel2 ...] into expr
        [SELECT TOP limit START AT record field1, field2]
        """
        if start == 1:
            sql = f"SELECT TOP {self._limit}"
        else:
            sql = f"SELECT TOP {self._limit} START AT {start}"

        return raw_sql.replace("SELECT", sql)

    def _source_model_record_count(self) -> int:
        """Calculate rows in DBF
        :rtype: object
        """
        sql = f"SELECT COUNT(*) as RECC FROM {self.source_model._meta.db_table};"
        rows = self._execute_query(sql)
        for row in rows:
            recc = row[0]
        return recc or 0

    def _get_models(self, app_name: str):
        return apps.get_app_config(app_name).get_models()

    def delete(self) -> bool:
        return self._delete_all_imported_records(model=self.dest_model)