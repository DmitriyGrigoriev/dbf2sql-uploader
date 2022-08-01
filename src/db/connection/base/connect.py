import pyodbc
from django.utils.translation import gettext_lazy as _
from .mixins import ODBCMixin, DataSourceMixin
from .dataclasses import FieldInfo

# ------------------------------------
# Base class
# ------------------------------------
class Connection(object):
    """
    This is the base/super class for different connection classes
    """
    ODBC_CLASS = None

    def __init__(self, **kwargs):
        """
        Initialization for the base class
        """
        self.drivers = []
        self.datasources = []
        self.maindriver = None

        if self.ODBC_CLASS is None:
            raise ValueError(_('ODBC_CLASS is required!'))
        else:
            self.odbc = self.ODBC_CLASS()

        if kwargs:
            for k, v in kwargs.items():
                if hasattr(self.odbc, k):
                    setattr(self.odbc, k, v)


    def pyodbc_drivers(self):
        """
        This function can be used to provide a list of drivers in pyodbc
        """
        print(_('The following drivers are provided: '))

        for driver in pyodbc.drivers():
            self.drivers.append(driver)
            print(str(driver))

    def driver_check(self, driver=None):
        """
        This function is used to check if driver exists for a specific type of connection
        """
        return [x for x in pyodbc.drivers() if x.startswith(driver)]


    def pyodbc_datasources(self):
        """
        This function can be used to provide a list of data sources in pyodbc
        """
        print(_('The following data sources are provided: '))

        for datasources in pyodbc.dataSources():
            self.datasources.append(datasources)
            print(str(datasources))


    def datasources_check(self, dsn=None):
        """
        This function is used to check if DSN exists for a specific type of connection
        """
        return [x for x in pyodbc.dataSources() if x.startswith(dsn)]


# ------------------------------------
# Connection to advantage sql server
# ------------------------------------
class DataSourceBaseConnect(DataSourceMixin, Connection):

    def __init__(self,
                 dsn: str = None,
                 uid=None,
                 pwd=None) -> None:

        '''

        Initialization of the class

        '''

        # Initialization inherited from the base class
        super().__init__()

        if dsn is None:
            dsn = self.odbc.dsn
        else:
            self.odbc.dsn = dsn

        self.odbc.check_credentials(uid=uid, pwd=pwd)

        # Initialize the connection
        self.make_connection()

        def make_connection(self):
            raise NotImplementedError(_('subclasses of DataSourceBaseConnect may require a make_connection() method'))


# ------------------------------------
# Base connection by ODBC drivers
# ------------------------------------
class ODBCBaseConnect(ODBCMixin, Connection):
    """
    This is a class to facilitate connection to SQL server databases using Python implementation of ODBC (pyodbc).

    Parameters:
        server (str): Server name/address for connection
        database (str): Database name/initial catalog
        trusted_connection (bool): True if ``Windows Authentication`` is used
        uid (str) : User ID to login and access the server
        pwd (str) : Password

    Example:

        Quick connection into local server:

        >>> connection=ODBCTools.AdvanatageClipper()

    .. codeauthor:: Mostafa Hadavand 2017-26-7

    """

    def __init__(self,
                 driver: str = None,
                 encoding: str = None,
                 data_directory: str = None,
                 uid=None,
                 pwd=None,
                 **kwargs
                 ) -> None:

        """

        Initialization of the class

        """

        # Initialization inherited from the base class
        super().__init__(**kwargs)

        if driver is None:
            driver = self.odbc.driver
        else:
            self.odbc.driver = driver

        if data_directory is None:
            raise ValueError(_("Property data_directory has not be empty"))
        else:
            self.odbc.data_directory = data_directory

        if encoding is None:
            self.encoding = self.odbc.encoding
        else:
            self.odbc.encoding = encoding

        if uid is None and len(self.odbc.uid) > 0:
            uid = self.odbc.uid

        self.odbc.check_credentials(uid=uid, pwd=pwd)

        # Initialize the connection
        self.make_connection()

        def make_connection(self):
            raise NotImplementedError(_('subclasses of AdvantageBaseConnect may require a make_connection() method'))


        def close(self):
            """
            A method to close the MS Access connection

            Example:

                >>> EDW_Access.close()

            """

            self.connection.close()

    def execute(self, command, **kwargs):
        '''
        This function can be used to deploy and commit a sql command into the target sql server using the inital catalog
        that is set during the initialization of PythonTools.ServerConnect

        Parameters:
            command (str): the command that is passed to the assigned server and database

        Example:

            >>> df = EDW_Access.execute(deploy)

        '''
        try:
            cursor = self.connection.cursor(**kwargs)
            cursor.execute(command, **kwargs)
            self.connection.commit()
            cursor.close()
        except Exception as e:
            raise RuntimeError(str(e))

        return cursor

    # def get_tables(self) -> list:
    #     return [t[2] for t in self.connection.cursor().tables().fetchall()]
    #
    #
    # def get_fields(self, table_name: str) -> dict:
    #     fields = self.connection.cursor().columns(table=table_name).fetchall()
    #     return {
    #         f[3]:
    #         FieldInfo(
    #             table=table_name,
    #             field_name=f[3],
    #             field_type=f[5],
    #             precision=f[6],
    #             scale=f[8],
    #             nullable=bool(f[10]),
    #             default=f[12]
    #         ) for f in fields
    #     }
