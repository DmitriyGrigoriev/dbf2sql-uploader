import os
import inspect
import logging
from pathlib import Path
from importlib import import_module
from django.db import connections
from django.utils.connection import ConnectionDoesNotExist
from django.utils.module_loading import module_has_submodule
from django.db import models
from src.config import settings

logger = logging.getLogger(__name__)


class BaseImport:

    def get_connection_by_alias(self, alias: str) -> connections:
        """Check connection using the connection name, see DATABASES section"""
        try:
            if alias in connections:
                return connections[alias]
            else:
                raise ConnectionDoesNotExist(alias)
        except Exception as e:
            logger.exception(e)
            raise e


    def get_databases_item_value(self, alias: str, key: str)-> str:
        """Return value from settings.DATABASES dict"""
        if alias is None:
            alias = "default"

        if alias in settings.DATABASES:
            data_dir_or_file = settings.DATABASES[alias][key]
            db_item_value = os.path.basename(data_dir_or_file)
            if db_item_value == '':
                db_item_value = Path(data_dir_or_file).parts[-1]
            return db_item_value

        return None


    def get_list_classes(self, entry, module_name, base_class)-> list:

        try:
            app_module = import_module(entry)
        except Exception as e:
            logger.exception(e)
            raise e

        res_models = []

        if module_has_submodule(app_module, module_name):
            mod_path = "%s.%s" % (entry, module_name)
            mod = import_module(mod_path)
            # Check if there's exactly one AppConfig candidate,
            # excluding those that explicitly define default = False.

            res_models = [
                (name, candidate)
                for name, candidate in inspect.getmembers(mod, inspect.isclass)
                if (
                        issubclass(candidate, base_class) and candidate is not base_class
                )
            ]

        return res_models


    def get_list_tables_from_model_class(self, entry: str, module_name: str)-> list:
        """Return list of table names selected in the db_table property Meta class"""
        return [klass._meta.db_table for _, klass in self.get_list_classes(entry, module_name, models.Model)]


    def get_model_class(self, entry: str, module_name: str, db_table: str)-> models:
        """Return model associated with the db_table property Meta class"""
        return [
            klass for _, klass in self.get_list_classes(entry, module_name, models.Model)
            if (
                    klass._meta.db_table.lower() == db_table.lower()
            )
        ][0]() or None
