import tablib
from src.services.base.baseimport import BaseImport
from src.services.sqllocal import SQLLocalFts
from src.apps.common.dataclasses import ETL, ImportInfo


def datetime_as_string(value):
    return value.strftime("%m/%d/%Y, %H:%M:%S")
    # ref: https://github.com/mkleehammer/pyodbc/issues/134#issuecomment-281739794
    # tup = struct.unpack("<6hI2h", dto_value)  # e.g., (2017, 3, 16, 10, 35, 18, 500000000, -6, 0)
    # return datetime(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5], tup[6] // 1000,
    #                 timezone(timedelta(hours=tup[7], minutes=tup[8])))


class SQLImport(BaseImport):
    def __init__(self, params: ImportInfo) -> None:
        # params = ImportInfo.from_dict({'table_pk': 174, 'poll_pk': 2, 'source_connection_name':
        # 'dbf_2022_test', 'source_table_name': 'DCLTECHD', 'dest_connection_name': 'test',
        # 'dest_table_name': 'TDCLTECHD', 'data_directory': 'TDCLTECHD', 'type': 'DBF',
        # 'last_write': '2022-08-26T11:24:36.911358', 'upload_record': 9534, 'table_record': 0,
        # 'status': 'enqueued', 'redis_message_id': '82dbcee0-17ee-4d81-bd43-a9f35b010b98'})
        # self._params = params
        self.partial_uploaded = False
        self._prev_start = 0
        super(SQLImport, self).__init__(params)

    def run_import(self) -> int:
        """Process importing data from DBF to SQL Server"""
        ##########################################################################
        # First step: GTD_2022_SMOLENSK.DCLHEAD.DBF -> GTD_2022_SMOLENSK.TDCLHEAD
        # SQLImport({
        #     source_connection_name: 'dbf_2022_smolensk'
        #     source_table_name: 'DCLHEAD',
        #     dest_connection_name: 'gtd_2022_smolensk',
        #     dest_table_name: 'TDCLHEAD'}
        # ).start_import()
        ##########################################################################
        try:
            self._reccount = self.dbf_record_count()
            if self._reccount > 0:
                self._delete_all_imported_records(model=self.dest_model)
                raw_sql_select = self._get_export_raw_sql()
                # resource = self._create_resource_instance()

                for i in reversed(range(0, self._reccount, self._limit)):
                    # select data from dbf model
                    sql = self._transform_raw_select(i, raw_sql=raw_sql_select)
                    rows = self._execute_query(sql)
                    dataset = tablib.Dataset(headers=self.headers)

                    for row in rows:
                        dataset.append(row=row)
                    self.resource.import_data(dataset, use_transactions=False, raise_errors=True)
                    # After importing some specific records from the end of the dbf file will
                    # run export to localfts database and continue import
                    if not self.partial_uploaded and (
                            self._reccount - i >= ETL.BULK.BATCH_SLICE
                    ):
                        self.export_to_localfts(is_partial=True)
                ######################################################################
                # Second step: GTD_2022_SMOLENSK.dbo.TDCLHEAD -> LocalFts.dbo.TDCLHEAD
                # SQLLocalFts({
                #     source_connection_name: 'gtd_2022_smolensk',
                #     source_table_name: 'TDCLHEAD',
                #     dest_connection_name: 'localfts',
                #     dest_table_name: 'TDCLHEAD',
                #     export_database_name: 'gtd_2022_smolensk'}
                # ).start_import()
                #######################################################################
                # Update LocalFts
                self.export_to_localfts(is_partial=False)
                self._reccount = self.imported_record_count()
        except Exception as e:
            self.logger.error(f'Error occurred in connection [{self.dest_connection_name}] '
                              f'table name: {self.dest_table_name}')
            self.logger.exception(e)
            raise e

        return self._reccount

    def imported_record_count(self) -> int:
        """Calculate imported rows"""
        result = self.dest_model.__class__.objects.using(self.dest_connection_name).count()

        return result

    def save_start_point(self, i: int):
        self._prev_start = i

    def export_to_localfts(self, is_partial: bool = False) -> None:
        if is_partial:
            self.partial_uploaded = is_partial
        export_to_fts = SQLLocalFts(self.params, is_partial=is_partial)
        export_to_fts.run_import()
        # Revert _db for property source_model and dest_model !Important
        # super(SQLImport, self).__init__(self._params)
        # self.resource = self._create_resource_instance()

    def _transform_raw_select(self, start: int, raw_sql: str, reverse: bool = False) -> str:
        """Transform SQL expr [SELECT field1, field2 ...] into expr
        [SELECT TOP limit START AT record field1, field2]
        """
        if start == 0:
            if self._prev_start == 0:
                sql = f"SELECT TOP {self._limit}"
            else:
                sql = f"SELECT TOP {self._limit-1}"
        else:
            sql = f"SELECT TOP {self._limit} START AT {start}"
        self.save_start_point(start)

        sql = raw_sql.replace("SELECT", sql)
        if self.logger:
            self.logger.info(f"{sql}")

        return sql

