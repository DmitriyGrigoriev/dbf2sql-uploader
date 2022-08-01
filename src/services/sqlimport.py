import tablib
import datetime
import logging
from django.db import models
from django.apps import apps
from import_export import resources
from src.services.base.baseimport import BaseImport
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
    _source_connection_name = None
    _dest_connection_name = None
    _source_model = None
    _dest_model = None
    _limit = settings.BATCH_SIZE
    _reccount = 0


    def __init__(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str, logger=None
                 ) -> None:

        ###########################################################################
        # First setting connection and then attach using_db to source model
        ###########################################################################
        self.source_model = self.get_model_class(settings.EXPORT_MODULE, 'models', source_table_name)
        self.source_connection_name = source_connection_name

        ###########################################################################
        # First setting connection and then attach using_db to destination model
        ###########################################################################
        self.dest_model = self.get_model_class(settings.IMPORT_MODULE, 'models', dest_table_name)
        self.dest_connection_name = dest_connection_name

        self.headers = self._get_exported_headers()

        # self.resources = self.populate(installed_apps=settings.INSTALLED_RESOURCE_APPS)
        self.resources = dict(
            self.get_list_classes(
                settings.IMPORT_MODULE,
                settings.RESOURCE_MODULE_NAME,
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
                    r = [r.isoformat() if (isinstance(r, datetime.date) | isinstance(r, datetime.datetime)) else r for r in
                         row]
                    dataset.append(row=r)

                resource = self._create_resource_instance()
                resource.import_data(dataset)

        except Exception as e:
            logger.exception(e)
            raise e

        return self._reccount


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


    def _create_resource_instance(self):
        res_model = self._get_resource_models()
        try:
            res_model.database = self.get_databases_item_value(
                alias=self.source_connection_name,
                key='NAME'
            ).lower()
        except AttributeError:
            pass
        return res_model


    def _get_resource_models(self)-> resources.ModelResource:
        for name, model in self.resources.items():
            if model.Meta.model.__name__.lower() == self.dest_model._meta.model.__name__.lower():
                return model()
        return None


    def _execute_query(self, row_sql: str)-> list:
        """Return rows by executing query SELECT * from dbf_model"""
        #self.source_connection
        return self.source_connection.cursor().execute(row_sql)


    def _get_export_raw_sql(self) -> str:
        """Return raw sql for export DBF model"""
        return self.source_model.__class__.objects.all().query.__str__()


    def _get_exported_headers(self)-> list:
        """Return fields list from DBF model"""
        return [field.attname for field in self.source_model._meta.fields]


    # def _get_model_instanse(self, model_name: str) -> models:
    #     app_models = []
    #     for app_name in apps.app_configs.keys():
    #         [app_models.append((app_name, model)) for model in self._get_models(app_name) \
    #          if model.__name__.lower() == model_name.lower()]
    #
    #     if len(app_models) > 1:
    #         raise RuntimeError(
    #             "%r declares more than one models with the same name: "
    #             "%s." % (app_models[0][0], app_models[0][1].__name__))
    #     elif len(app_models) == 0:
    #         raise RuntimeError("No one model was declared.")
    #
    #     return app_models[0][1]


    def _get_models(self, app_name: str):
        return apps.get_app_config(app_name).get_models()


    def _delete_all_imported_records(self, model: models)-> bool:
        # clearing down existing objects
        try:
            model.__class__.objects.using(self.dest_connection.alias).all().delete()
        except Exception as e:
            logger.exception(e)
            raise e

        return True


    # setter
    def set_source_model(self, value):
        """Set property to the source model and define what connect we will be using farther"""
        self._source_model = value
        if self.source_connection_name:
            self.source_model._meta.model.objects._db = self.source_connection_name


    #getter
    def get_source_model(self):
        return self._source_model


    source_model = property(get_source_model, set_source_model)


    # setter
    def set_dest_model(self, value):
        self._dest_model = value
        if self.dest_connection_name:
            self.dest_model._meta.model.objects._db = self._dest_connection_name


    #getter
    def get_dest_model(self):
        return self._dest_model

    dest_model = property(get_dest_model, set_dest_model)


    # setter
    def set_source_connection_name(self, value):
        self._source_connection_name = value
        if self.source_model:
            self.source_model._meta.model.objects._db = self._source_connection_name

        self.source_connection = self.get_connection_by_alias(self.source_connection_name)


    #getter
    def get_source_connection_name(self):
        return self._source_connection_name

    source_connection_name = property(get_source_connection_name, set_source_connection_name)

    # setter
    def set_dest_connection_name(self, value: str):
        self._dest_connection_name = value
        if self.dest_model:
            self.dest_model._meta.model.objects._db = self._dest_connection_name

        self.dest_connection = self.get_connection_by_alias(self.dest_connection_name)

    #getter
    def get_dest_connection_name(self):
        return self._dest_connection_name

    dest_connection_name = property(get_dest_connection_name, set_dest_connection_name)


# class Resource:
#
#     def __init__(self, installed_apps=()):
#         if installed_apps is None :
#             raise RuntimeError("You must supply an installed_apps argument.")
#
#         # Mapping of labels to AppConfig instances for installed apps.
#         self.res_models = {}
#
#     def populate(self, installed_apps=None):
#
#         for entry in installed_apps:
#             # If import_module succeeds, entry points to the resource app module.
#             try:
#                 app_module = import_module(entry)
#             except Exception as e:
#                 logger.exception(e)
#                 raise e
#
#             if module_has_submodule(app_module, RESOURCE_MODULE_NAME):
#                 mod_path = "%s.%s" % (entry, RESOURCE_MODULE_NAME)
#                 mod = import_module(mod_path)
#                 # Check if there's exactly one AppConfig candidate,
#                 # excluding those that explicitly define default = False.
#                 res_models = [
#                     (name, candidate)
#                     for name, candidate in inspect.getmembers(mod, inspect.isclass)
#                     if (
#                             issubclass(candidate, ModelResource)
#                             and candidate is not ModelResource
#                     )
#                 ]
#                 self.res_models = dict(res_models)
#
#         return  self.res_models
#
#         #     if isinstance(entry, ResourceConfig):
#         #         app_config = entry
#         #     else:
#         #         app_config = ResourceConfig.create(entry)
#         #     if app_config._meta.model.lower() in self.app_configs:
#         #         raise ImproperlyConfigured(
#         #             "Resource tables aren't unique, "
#         #             "duplicates: %s" % app_config.label
#         #         )
#         #
#         #     self.app_configs[app_config._meta.model.lower()] = app_config
#         #     app_config.apps = self
