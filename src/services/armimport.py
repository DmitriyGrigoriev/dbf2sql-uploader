import tablib
import logging
import datetime
from dateutil.relativedelta import relativedelta
from django.db.models import Count
from import_export import resources
from src.services.base.baseimport import BaseImport
from src.config import settings


logger = logging.getLogger(__name__)


class ARMImport(BaseImport):
    delete_imported_records = True
    _period_of_month = -2 # get export data for 2 last month
    _type = 'ARM'


    def __init__(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str, logger=None
                 ) -> None:
        self.source_table_name = source_table_name
        self.dest_table_name = dest_table_name

        ###########################################################################
        # First setting connection and then attach using_db to source model
        ###########################################################################
        self.source_model = self.get_model_class(
            settings.PIPE_MODULES['ARM']['export'], 'models', self.source_table_name
        )
        self.source_connection_name = source_connection_name

        ###########################################################################
        # First setting connection and then attach using_db to destination model
        ###########################################################################
        self.dest_model = self.get_model_class(
            settings.PIPE_MODULES['ARM']['import'], 'models', self.dest_table_name
        )
        self.dest_connection_name = dest_connection_name

        self.headers = self._get_exported_headers()

        self.resources = dict(
            self.get_list_classes(
                settings.PIPE_MODULES['ARM']['import'], # import module
                settings.PIPE_MODULES['ARM']['resource'], # resource module
                resources.ModelResource
            )
        )

        self.logger = logger or None


    def start_import(self):
        """Process importing data from DBF to SQL Server"""
        try:
            if self.delete_imported_records:
                self._delete_all_imported_records(model=self.dest_model)

            self._reccount = self._source_model_record_count()
            today = datetime.date.today()
            last = self.gomonth(today=today, month=self._period_of_month)
            # raw_sql = self._get_export_raw_sql()

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

                resource = self._create_resource_instance()
                resource.import_data(dataset)
            #
            #     # Update LocalFts
            #     self.after_import(
            #         source_connection_name=self.source_connection_name,
            #         source_table_name=self.source_table_name,
            #         dest_connection_name=self.dest_connection_name,
            #         dest_table_name=self.dest_table_name,
            #         logger=self.logger
            #     )

        except Exception as e:
            logger.exception(e)
            raise e

        return self._reccount


    def _transform_raw_select(self, start: int, raw_sql: str) -> str:
        """Transform SQL expr [SELECT field1, fiel2 ...] into expr
        [SELECT field1, field2 WHERE ...]
        """
        field = self._exported_field_exist('g072')
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
        field = self._exported_field_exist('g072')

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
