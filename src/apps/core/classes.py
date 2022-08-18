import json
from pathlib import Path
from django.db import connections
from django.contrib import messages
from django.core.management import call_command
from django.utils.translation import gettext_lazy as _
from src.config import settings

from .models import ConnectWrapper


class ConnectBaseValidator:
    _error_numbers = ()
    _error = False
    conn_wrapper = ConnectWrapper()

    def __init__(self, request, form, change):
        self.request = request
        self.form = form
        self.change = change
        self.connection_id = self.get_slug_name()
        self.database_name = form.cleaned_data['name']
        self.engine = form.cleaned_data['engine']


    def validate(self):
        raise NotImplementedError('subclasses of ConnectBaseValidator must provide a validate() method')


    def get_slug_name(self):
        return self.conn_wrapper.get_slug_name(conname=self.form.cleaned_data['conname']).lower()


    def get_database_name(self):
        if self.database_name:
            return self.database_name
        else:
            raise ValueError(_("Database name is empty"))


    def _show_error_message(self, e):
        error_message = e.args[1]
        show_error = False
        for error_number in self._error_numbers:
            if error_number in error_message:
                messages.error(self.request, "%s" % error_message)
                self._error = True
                show_error = True
        return show_error


    def get_internal_db_connection(self):
        return connections[self.connection_id]


    def database_exists(self):
        raise NotImplementedError('subclasses of ConnectBaseValidator must provide a database_exists() method')


    def drop_database(self):
        messages.info(self.request, "%s" % _(f"Link to the database {self.database_name} was successful deleted. "
                                        f"The physical data has not yet been deleted. You can do this manually later. "))


    def _connection_params(self):
        raise NotImplementedError('subclasses of ConnectBaseValidator must provide a _connection_params() method')


class SQLConnectValidator(ConnectBaseValidator):
    _error_numbers = ('42000','28000','08001',)

    def validate(self):
        if self._connection_params():
            try:
                if self.database_exists() is None:
                    self.create_database()
                    messages.info(self.request, "%s" % _(f"Database {self.database_name} was successful created."))
            except Exception as e:
                if not self._show_error_message(e):
                    raise
        return True


    def _connection_params(self):
        success = True
        cleaned_data = self.form.cleaned_data
        connection_params = {} if not self.connection_id in settings.DATABASES else settings.DATABASES[self.connection_id]
        try:
            connection_params["ENGINE"] = cleaned_data['engine']
            connection_params["NAME"] = 'tempdb'  # need database name for connection
            connection_params["USER"] = cleaned_data['user']
            connection_params["PASSWORD"] = cleaned_data['password']
            connection_params["HOST"] = cleaned_data['host']
            connection_params["PORT"] = cleaned_data['port']
            connection_params["OPTIONS"] = json.loads(cleaned_data['options'].replace("'", "\""))

            settings.DATABASES[self.connection_id] = connection_params

        except Exception as e:
            success = False
        return success


    def get_temporary_connection(self):
        backend_databasewrapper = self.get_internal_db_connection()
        return backend_databasewrapper.temporary_connection()


    def database_exists(self):
        with self.get_temporary_connection() as cursor:
            return cursor.execute("SELECT DB_ID('%s') AS DatabaseID" % (self.get_database_name())).fetchone()[0]


    def create_database(self)-> None:
        with self.get_temporary_connection() as cursor:
            cursor.execute('CREATE DATABASE "%s" ' % (self.get_database_name()))
        # Replace "tempdb" database name to real name
        settings.DATABASES[self.connection_id]["NAME"] = self.database_name
        call_command('migrate', 'sqlimport', database=self.connection_id,
                     interactive=False, verbosity=0)



class DBFConnectValidator(ConnectBaseValidator):

    def validate(self):
        if self._connection_params():
            try:
                if self.database_exists() is None:
                    messages.error(self.request, "%s" % _(
                        f"The path to the data directory {self.database_name} not found, please check it."))
            except Exception as e:
                if not self._show_error_message(e):
                    raise
        return True


    def _connection_params(self):
        success = True
        cleaned_data = self.form.cleaned_data
        connection_params = {} if not self.connection_id in settings.DATABASES else settings.DATABASES[self.connection_id]
        try:
            connection_params["ENGINE"] = cleaned_data['engine']
            connection_params["NAME"] = cleaned_data['name']
            connection_params["USER"] = cleaned_data['user']
            connection_params["PASSWORD"] = cleaned_data['password']
            connection_params["HOST"] = cleaned_data['host']
            connection_params["PORT"] = cleaned_data['port']
            connection_params["OPTIONS"] = json.loads(cleaned_data['options'].replace("'", "\""))

            settings.DATABASES[self.connection_id] = connection_params

        except Exception as e:
            success = False
        return success


    def database_exists(self):
        return 1 if Path(self.get_database_name()).is_dir() else None


    def create_database(self) -> None:
        pass
