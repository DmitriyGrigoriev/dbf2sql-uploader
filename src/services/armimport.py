import tablib
import logging
import datetime
from dateutil.relativedelta import relativedelta
from src.services.base.baseimport import BaseImport
from src.services.armlocal import ARMLocalFts
from src.apps.common.dataclasses import ETL

logger = logging.getLogger(__name__)

class ARMImport(BaseImport):

    def __init__(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str, logger=None,
                 mode: str = ETL.MODE.FULL
                 ) -> None:

        super(ARMImport, self).__init__()

        self.type = ETL.EXPORT.DOC2SQL
        self._period_of_month = -10  # get export data for 10 last month
        self.source_model_module = ETL.PIPE_MODULES.DOC2SQL_EXPORT
        self.dest_model_module = ETL.PIPE_MODULES.DOC2SQL_IMPORT

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
        try:
            if self.mode == ETL.MODE.FULL or self.mode == ETL.MODE.IMPORT:
                # if self.delete_imported_records:
                self._delete_all_imported_records(model=self.dest_model)

                self._reccount = self._source_model_record_count()
                today = datetime.date.today()
                last = self.gomonth(today=today, month=self._period_of_month)
                resource = self._create_resource_instance()

                for start in range(0, self._reccount, self._limit):
                    # select data from model
                    sql = self._transform_raw_select(start=start, raw_sql='')

                    if self.logger:
                        self.logger.info(f"Execute SQL: {sql}")

                    # rows = self.source_model.__class__.objects.using(self.source_connection_name).\
                    #              raw(sql, [last, today])[start + 1:self._limit]

                    rows = self._execute_query(sql, params=[last, today])

                    dataset = tablib.Dataset(headers=self.headers)

                    for row in rows:
                        dataset.append(row=row)

                    resource.import_data(dataset, use_transactions=False)
                    dataset.wipe()

                    if self.mode == ETL.MODE.FULL or self.mode == ETL.MODE.EXPORT:
                        # Update LocalFts
                        self.after_import(
                            source_connection_name=self.source_connection_name,
                            source_table_name=self.source_table_name,
                            dest_connection_name=self.dest_connection_name,
                            dest_table_name=self.dest_table_name,
                            logger=self.logger,
                            mode=self.mode
                        )

        except Exception as e:
            logger.info(f'Error occured in: {self.dest_connection_name} table {self.dest_table_name}')
            logger.exception(e)
            raise e

        return self._reccount

    def after_import(self, source_connection_name: str, source_table_name: str,
                     dest_connection_name: str, dest_table_name: str, logger: str =None,
                     mode: str = ETL.MODE.FULL
                 ) -> None:
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
        # Second step: gtd_arm_test.DCLHEAD -> localfts.TDCLHEAD
        # ARMLocalFts(
        #     source_connection_name='gtd_arm_test',
        #     source_table_name='DBRHEAD',
        #     dest_connection_name='localfts',
        #     dest_table_name='TDCLHEAD',
        #     logger=None
        # ).start_import()
        #######################################################################
        ARMLocalFts(
            source_connection_name=dest_connection_name,
            source_table_name=dest_table_name,
            dest_connection_name=ETL.CONNECT.LOCALFTS,
            dest_table_name=ETL.PIPE_MODULES.DBF_TABLE_PREFIX + dest_table_name,
            logger=logger,
            mode=mode
        ).start_import()

        # Restore using_db
        self.restore_default(
            source_connection_name, source_table_name,
            dest_connection_name, dest_table_name, logger=None,
            mode=mode
        )

    def _transform_raw_select(self, start: int, raw_sql: str) -> str:
        """Transform SQL expr [SELECT field1, fiel2 ...] into expr
        [SELECT field1, field2 WHERE ...]
        """
        field = self._exported_field_exist(ETL.FIELD.G072)
        if start == 0:
            row_sql = self.source_model.__class__.objects.\
                          using(self.source_connection_name)\
                          [start:self._limit].query.__str__()
        else:
            row_sql = self.source_model.__class__.objects.\
                          using(self.source_connection_name)\
                          [start:self._limit+start].query.__str__()

        order_index = row_sql.find('ORDER BY')

        if order_index >=0:
            limit = row_sql[order_index:]
            row_sql = row_sql[0:order_index]
        else:
            limit = ''

        if field:
            where = f" WHERE ([{field}] >= %s AND [{field}] <= %s)"
        else:
            where = ""
        return f"{row_sql}{where} {limit}"

    def _imported_field_exist(self, field: str):
        result = [
            field
            for f in self._get_imported_headers()
                if f.lower() == field.lower()
        ]
        return result or None

    def _exported_field_exist(self, field: str):
        result = [
            field
            for f in self._get_exported_headers()
                if f.lower() == field.lower()
        ]
        return result[0] or None

    def gomonth(self, today: datetime.date, month: int):
        return today + relativedelta(months=+month)

    def _source_model_record_count(self) -> int:
        """Calculate was exported rows"""
        field = self._exported_field_exist(ETL.FIELD.G072)

        today = datetime.date.today()
        last = self.gomonth(today=today, month=self._period_of_month)

        if field:
            result = self.source_model.__class__.objects.using(self.source_connection_name). \
                    filter(g072__gte=last, g072__lte=today).count()
        else:
            result = self.source_model.__class__.objects.using(self.source_connection_name).count()

        return result

        # result = len(self.source_model.__class__.objects.using(self.source_connection_name). \
        #            filter(g072__gte=last, g072__lte=today).all())

        # if field:
            # first_date = self.convert_datetime_format_to_sql_compatible(self.gomonth(today=today, month=-2))
            # second_date = self.convert_datetime_format_to_sql_compatible(today)

            # recc = len(self.source_model.__class__.objects.using(self.source_connection_name). \
            #     filter(g072__gte=last, g072__lte=today).all())

            # sql = self.source_model.__class__.objects.\
            #     using(self.source_connection_name).values(field). \
            #     annotate(Count(field)).\
            #     filter(g072__gte=first_date, g072__lte=second_date)

        # else:
        #     sql = self.source_model.__class__.objects.\
        #             values(field).annotate(Count(field)). \
        #             query.__str__()

        # rows = self._execute_query(sql)
        # for row in rows:
        #     recc = row[0]
        # return result
