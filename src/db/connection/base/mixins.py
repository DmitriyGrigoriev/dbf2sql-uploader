import pyodbc
from pydantic import ValidationError

class BaseMixin(object):

    def make_connection(self):
        '''
        Initializing connection to advantage database server open: clipper dbf files
        '''

        try:
            connection_string = self.odbc.make_connection_string()

        except ValidationError as e:

            raise e


        try:
            if hasattr(self.odbc, 'encoding') and len(self.odbc.encoding) > 0:
                self.connection = pyodbc.connect(connection_string, ansi=True)
                self.connection.setdecoding(pyodbc.SQL_CHAR, encoding=self.odbc.encoding)
            else:
                self.connection = pyodbc.connect(connection_string)
            # self.connection = pyodbc.connect(connection_string, ansi=True)

        except Exception as e:

            raise ConnectionError('Failed to Connect to server\n' + str(e))

        print('Successful Connection')


class ODBCMixin(BaseMixin):

    def check_drivers(self):
        sql_drivers = super().driver_check(driver=self.odbc.driver)
        if len(sql_drivers) == 0:
            super().pyodbc_drivers()
            raise ValueError(f"ODBC driver {self.odbc.driver} not found...")

        else:
            self.maindriver = sql_drivers[0]


    def make_connection(self):
        self.check_drivers()
        super().make_connection()


class DataSourceMixin(BaseMixin):

    def check_datasources(self):
        '''
        Check installed DSN data sources
        '''
        sql_datasources = super().datasources_check(dsn=self.odbc.dsn)
        if len(sql_datasources) == 0:
            super().pyodbc_datasources()
            raise ValueError(f"DSN data sources {self.odbc.dsn} not found...")

        else:
            self.maindriver = sql_datasources[0]

    def make_connection(self):
        self.check_datasources()
        super().make_connection()