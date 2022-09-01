import tablib
import datetime
import logging
from django.apps import apps
from import_export import resources
from src.services.base.baseimport import BaseImport
from src.services.sqllocal import SQLLocalFts
from src.config import settings


logger = logging.getLogger(__name__)


def datetime_as_string(value):
    return value.strftime("%m/%d/%Y, %H:%M:%S")
    # ref: https://github.com/mkleehammer/pyodbc/issues/134#issuecomment-281739794
    # tup = struct.unpack("<6hI2h", dto_value)  # e.g., (2017, 3, 16, 10, 35, 18, 500000000, -6, 0)
    # return datetime(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5], tup[6] // 1000,
    #                 timezone(timedelta(hours=tup[7], minutes=tup[8])))


class SQLImport(BaseImport):
    delete_imported_records = True
    _type = 'DBF'


    def __init__(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str, logger=None
                 ) -> None:
        self.source_table_name = source_table_name
        self.dest_table_name = dest_table_name

        ###########################################################################
        # First setting connection and then attach using_db to source model
        ###########################################################################
        self.source_model = self.get_model_class(
            settings.PIPE_MODULES['DBF']['export'], 'models', self.source_table_name
        )
        self.source_connection_name = source_connection_name

        ###########################################################################
        # First setting connection and then attach using_db to destination model
        ###########################################################################
        self.dest_model = self.get_model_class(
            settings.PIPE_MODULES['DBF']['import'], 'models', self.dest_table_name
        )
        self.dest_connection_name = dest_connection_name

        self.headers = self._get_exported_headers()

        self.resources = dict(
            self.get_list_classes(
                settings.PIPE_MODULES['DBF']['import'], # import module
                settings.PIPE_MODULES['DBF']['resource'], # resource module
                resources.ModelResource
            )
        )

        self.logger = logger or None

        # self._add_datetime_output_conversion_funct()


    def start_import(self):
        """Process importing data from DBF to SQL Server"""
        try:
            if self.delete_imported_records:
                self._delete_all_imported_records(model=self.dest_model)

            self._reccount = self._source_model_record_count()
            raw_sql = self._get_export_raw_sql()

            for start in range(0, self._reccount, self._limit):
                # select data from dbf model
                sql = self._transform_raw_select(start=start + 1, raw_sql=raw_sql)

                if self.logger:
                    self.logger.info(f"Execute SQL: {sql}")

                rows = self._execute_query(sql)
                dataset = tablib.Dataset(headers=self.headers)

                for row in rows:
                    """Replace datetime format to iso format like to YYYY-DD-MM"""
                    # r = [r.isoformat() if (isinstance(r, datetime.date) | isinstance(r, datetime.datetime)) else r for r in
                    #      row]
                    # dataset.append(row=r)
                    dataset.append(row=row)

                resource = self._create_resource_instance()
                resource.import_data(dataset)

                # Update LocalFts
                self.after_import(
                    source_connection_name=self.source_connection_name,
                    source_table_name=self.source_table_name,
                    dest_connection_name=self.dest_connection_name,
                    dest_table_name=self.dest_table_name,
                    logger=self.logger
                )

        except Exception as e:
            logger.info(f'Error occured in: {self.dest_connection_name} table {self.dest_table_name}')
            logger.exception(e)
            raise e

        return self._reccount


    def after_import(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str, logger=logger
                 ) -> None:
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
        #     logger=None
        # ).start_import()
        #######################################################################
        # SQLLocalFts(
        #     source_connection_name=source_connection_name,
        #     source_table_name=source_table_name,
        #     dest_connection_name=dest_connection_name,
        #     dest_table_name=dest_table_name,
        #     logger=logger
        # ).start_import()

        SQLLocalFts(
            source_connection_name=dest_connection_name,
            source_table_name=dest_table_name,
            dest_connection_name=settings.CONNECTION_FTS,
            dest_table_name=dest_table_name,
            logger=logger
        ).start_import()

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
        """Calculate rows in DBF"""
        sql = f"SELECT COUNT(*) as RECC FROM {self.source_model._meta.db_table};"
        rows = self._execute_query(sql)
        for row in rows:
            recc = row[0]
        return recc or 0

    # def _add_datetime_output_conversion_funct(self):
    #     if self.source_connection:
    #         self.source_connection.Database.Connection.add_output_converter(
    #             self.source_connection.Database.SQL_TYPE_TIMESTAMP, datetime_as_string
    #         )

    def _get_models(self, app_name: str):
        return apps.get_app_config(app_name).get_models()


