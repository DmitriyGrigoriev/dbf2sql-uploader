import json
from pathlib import Path
from typing import Optional
from typing import Tuple

from django.contrib import messages
from django.core.management import call_command
from django.db import connections
from django.db.utils import ConnectionHandler
from django.utils.translation import gettext_lazy as _

from .models import ConnectWrapper
from src.config import settings


class ConnectBaseValidator:
    _error_numbers: Tuple[str, str, str]
    _error = False
    conn_wrapper = ConnectWrapper()

    def __init__(self, request: object, connect: ConnectWrapper, type: str):
        """
        Initialize validator

        :param request:
        :param connect:
        :param type:
        """
        self.request = request
        self.connect = connect
        self.type: str = type
        self.connection_id: str = self.get_slug_name()
        self.database_name: str = self.connect.name
        self.engine: str = self.connect.engine

    def validate(self) -> bool:
        raise NotImplementedError(
            "subclasses of ConnectBaseValidator must provide a validate() method"
        )

    def get_slug_name(self) -> str:
        """
        Return slug connection name

        :return: connection name
        """
        return self.connect.slug_name.lower()
        # return self.conn_wrapper.get_slug_name(conname=self.form.cleaned_data['conname']).lower()

    def get_database_name(self) -> str:
        if self.database_name:
            return self.database_name
        else:
            raise ValueError(_("Database name is empty"))

    def _show_error_message(self, e: Exception) -> bool:
        """
        Show error message and return True if error occurred

        :param e:
        :return:
        """
        error_message = e.args[1]
        show_error = False
        for error_number in self._error_numbers:
            if error_number in error_message:
                messages.error(self.request, "%s" % error_message)
                self._error = True
                show_error = True
        return show_error

    def get_internal_db_connection(self) -> ConnectionHandler:
        return connections[self.connection_id]

    def database_exists(self) -> Optional[int]:
        raise NotImplementedError(
            "subclasses of ConnectBaseValidator must provide a database_exists() method"
        )

    def drop_database(self) -> None:
        messages.info(
            self.request,
            "%s"
            % _(
                f"Link to the database {self.database_name} was successful deleted. "
                f"The physical data has not yet been deleted. You can do this manually later. "
            ),
        )

    def _connection_params(self) -> bool:
        raise NotImplementedError(
            "subclasses of ConnectBaseValidator must provide a _connection_params() method"
        )


class SQLConnectValidator(ConnectBaseValidator):
    _error_numbers = (
        "42000",
        "28000",
        "08001",
    )

    def validate(self) -> bool:
        if self._connection_params():
            try:
                if self.database_exists() is None:
                    self.create_database()
                    messages.info(
                        self.request,
                        "%s"
                        % _(
                            f"Database {self.database_name} was successful created."
                        ),
                    )
            except Exception as e:
                if not self._show_error_message(e):
                    raise
        return True

    def _connection_params(self) -> bool:
        success = True
        # cleaned_data = self.form.cleaned_data
        connection_params = (
            {}
            if self.connection_id not in settings.DATABASES
            else settings.DATABASES[self.connection_id]
        )
        try:
            connection_params["ENGINE"] = self.engine
            connection_params[
                "NAME"
            ] = None  # need database name for connection
            connection_params["USER"] = self.connect.user
            connection_params["PASSWORD"] = self.connect.password
            connection_params["HOST"] = self.connect.host
            connection_params["PORT"] = self.connect.port
            connection_params["OPTIONS"] = json.loads(
                self.connect.options.replace("'", '"')
            )

            settings.DATABASES[self.connection_id] = connection_params

        except Exception:
            success = False
        return success

    def get_temporary_connection(self) -> ConnectionHandler:
        backend_databasewrapper = self.get_internal_db_connection()
        return backend_databasewrapper.temporary_connection()

    def database_exists(self) -> bool:
        with self.get_temporary_connection() as cursor:
            return cursor.execute(
                "SELECT DB_ID('%s') AS DatabaseID" % (self.get_database_name())
            ).fetchone()[0]

    def create_database(self) -> None:
        with self.get_temporary_connection() as cursor:
            cursor.execute(
                'CREATE DATABASE "%s" ' % (self.get_database_name())
            )
        # Replace "tempdb" database name to real name
        settings.DATABASES[self.connection_id]["NAME"] = self.database_name
        if self.type == "ARM":
            call_command(
                "migrate",
                "armimport",
                database=self.connection_id,
                interactive=False,
                verbosity=0,
            )
        else:
            call_command(
                "migrate",
                "sqlimport",
                database=self.connection_id,
                interactive=False,
                verbosity=0,
            )


class DBFConnectValidator(ConnectBaseValidator):
    def validate(self) -> bool:
        if self._connection_params():
            try:
                if self.database_exists() is None:
                    messages.error(
                        self.request,
                        "%s"
                        % _(
                            f"The path to the data directory {self.database_name} not found, please check it."
                        ),
                    )
            except Exception as e:
                if not self._show_error_message(e):
                    raise
        return True

    def _connection_params(self) -> bool:
        success = True
        # cleaned_data = self.form.cleaned_data
        connection_params = (
            {}
            if self.connection_id not in settings.DATABASES
            else settings.DATABASES[self.connection_id]
        )
        try:
            connection_params["ENGINE"] = self.connect.engine
            connection_params["NAME"] = self.connect.name
            connection_params["USER"] = self.connect.user
            connection_params["PASSWORD"] = self.connect.password
            connection_params["HOST"] = self.connect.host
            connection_params["PORT"] = self.connect.port
            connection_params["OPTIONS"] = json.loads(
                self.connect.options.replace("'", '"')
            )

            settings.DATABASES[self.connection_id] = connection_params

        except Exception:
            success = False
        return success

    def database_exists(self) -> Optional[int]:
        return 1 if Path(self.get_database_name()).is_dir() else None

    def create_database(self) -> None:
        pass
