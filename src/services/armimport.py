import copy
import tablib
import datetime
from src.services.base.baseimport import BaseImport
from src.services.armlocal import ARMLocalFts
from src.apps.common.dataclasses import ETL, ImportInfo


class ARMImport(BaseImport):
    def run_import(self):
        """Process importing data from DBF to SQL Server"""
        ######################################################################
        # First step: arm_edh.DBRHEAD -> gtd_arm_test.DCLHEAD
        # ARMImport(
        #     source_connection_name='arm_edh',
        #     source_table_name='DBRHEAD',
        #     dest_connection_name='gtd_arm_test',
        #     dest_table_name='DCLHEAD',
        #     logger=None
        # ).start_import()
        ######################################################################
        try:
            self._reccount = self.arm_record_count()
            if self._reccount > 0:
                self._delete_all_imported_records(model=self.dest_model)
                resource = self._create_resource_instance()

                for start in range(0, self._reccount, self._limit):
                    # select data from model
                    sql = self._transform_raw_select(start=start, raw_sql='')
                    # rows = self._execute_query(sql, params=[last, today])
                    rows = self._execute_query(sql)
                    dataset = tablib.Dataset(headers=self.headers)

                    for row in rows:
                        dataset.append(row=row)
                    resource.import_data(dataset, use_transactions=False, collect_failed_rows=True)
                ######################################################################
                # Second step: gtd_arm_test.DCLHEAD -> localfts.TDCLHEAD
                # ARMLocalFts(
                #     source_connection_name='gtd_arm_test',
                #     source_table_name='DBRHEAD',
                #     dest_connection_name='localfts',
                #     dest_table_name='TDCLHEAD',
                #     logger=None
                # ).start_import()
                #######################################################################
                # Update LocalFts
                self.export_to_localfts()
        # except ConnectionError:
        #     self.logger.warning(f"Failed to connection {self.dest_connection_name}.", exc_info=True)
        except Exception as e:
            self.logger.error(f'Error occurred in connection [{self.dest_connection_name}] '
                              f'table name: {self.dest_table_name}')
            self.logger.exception(e)
            raise e

        return self._reccount

    def export_to_localfts(self) -> None:
        params: ImportInfo = self.get_export_params()
        ARMLocalFts(params).run_import()

    def _transform_raw_select(self, start: int, raw_sql: str) -> str:
        """Transform SQL expr [SELECT field1, field2 ...] into expr
            [SELECT field1, field2 WHERE ...]
        """
        today = datetime.date.today()
        last = self.gomonth(today=datetime.date.today(), month=self._period_of_month)
        # field = self._exported_field_exist(ETL.FIELD.G072)
        if start == 0:
            # Important: Do not remove order by clause (using for correct offset)
            row_sql = self.source_model.__class__.objects.\
                using(self.source_connection_name).\
                filter(g072__gte=last,g072__lte=today).\
                order_by(self.source_model.__class__._meta.pk.name)\
                [start:self._limit].query.__str__()
        else:
            # Important: Do not remove order by clause (using for correct offset)
            row_sql = self.source_model.__class__.objects.\
                using(self.source_connection_name).\
                filter(g072__gte=last,g072__lte=today).\
                order_by(self.source_model.__class__._meta.pk.name)\
                [start:self._limit+start].query.__str__()

        row_sql = row_sql.replace(last.strftime("%Y-%m-%d %H:%M:%S"), f"'{last.strftime('%Y-%m-%d %H:%M:%S')}'")
        row_sql = row_sql.replace(today.strftime("%Y-%m-%d %H:%M:%S"), f"'{today.strftime('%Y-%m-%d %H:%M:%S')}'")

        if self.logger:
            self.logger.info(f"{row_sql}")

        return row_sql

    def get_export_params(self):
        params: ImportInfo = copy.copy(self.params)
        params.source_connection_name = self.params.dest_connection_name
        params.source_table_name = self.params.dest_table_name
        params.dest_connection_name = ETL.CONNECT.LOCALFTS
        params.dest_table_name = ETL.PIPE_MODULES.DBF_TABLE_PREFIX + self.params.dest_table_name
        return params
