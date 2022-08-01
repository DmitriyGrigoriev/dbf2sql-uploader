from .base.connect import ODBCBaseConnect, DataSourceBaseConnect
from .odbc import AdvanatageClipper, AdvanatageVisualFoxpro, DataSources

__all__ = ['AdvantageClipperConnect', 'AdvantageVisualFoxproConnect', 'ODBCDataSourceConnect']

class AdvantageClipperConnect(ODBCBaseConnect):
    ODBC_CLASS = AdvanatageClipper


class AdvantageVisualFoxproConnect(ODBCBaseConnect):
    ODBC_CLASS = AdvanatageVisualFoxpro


class ODBCDataSourceConnect(DataSourceBaseConnect):
    ODBC_CLASS = DataSources


# ------------------------------------
# Connection to sql server
# ------------------------------------
# class ServerConnect(Connection):
#     """
#     This is a class to facilitate connection to SQL server databases using Python implementation of ODBC (pyodbc).
#
#     Parameters:
#         server (str): Server name/address for connection
#         database (str): Database name/initial catalog
#         trusted_connection (bool): True if ``Windows Authentication`` is used
#         uid (str) : User ID to login and access the server
#         pwd (str) : Password
#
#     Example:
#
#         Quick connection into local server:
#
#         >>> connection=ODBCTools.ServerConnect(server='localhost',database='EdwInfoMartLocal', trusted_connection=True)
#
#     .. codeauthor:: Mostafa Hadavand 2017-26-7
#
#     """
#
#     def __str__(self):
#
#         return 'An object to facilitate connection to a sql server database'
#
#     def __init__(self, server=None, database=None, trusted_connection=True, uid=None, pwd=None):
#
#         '''
#
#         Initialization of the class
#
#         '''
#
#         # Initialization inherited from the base class
#         super().__init__()
#
#         # Sanity check
#         if server is None:
#             raise ValueError('server Name is required!')
#
#         if database is None:
#             database = 'master'
#             print('database Name sould be provided (masetr was chosen)!')
#
#         self.initial_catalog = database
#
#         try:
#             assert isinstance(server, str)
#             self.server = server
#             assert isinstance(database, str)
#             self.database = database
#         except:
#             raise ValueError('server/database entry must be string')
#
#         self.trusted_connection = trusted_connection
#
#         # Sanity check
#         if not self.trusted_connection:
#             if uid is None:
#                 raise ValueError('User ID is required for connection!')
#
#             if pwd is None:
#                 pwd = getpass.getpass("Password for " + uid + " :")
#
#             try:
#                 assert isinstance(uid, str)
#                 self.uid = uid
#                 assert isinstance(pwd, str)
#                 self.pwd = pwd
#             except:
#                 raise ValueError('uid/pwd entry must be string!')
#
#         # Initialize the connection
#         self.make_connection()
#
#     def make_connection(self):
#
#         '''
#         Initializing connection to sql server
#         '''
#
#         # check if the required ODBC drivers are installed and available
#         sql_drivers = super().driver_check(driver='SQL Server')
#         if len(sql_drivers) == 0:
#             super().pyodbc_drivers()
#             raise ValueError('Driver for SQL server was not found...')
#
#         else:
#             self.maindriver = sql_drivers[0]
#
#         if self.trusted_connection:
#
#             connection_string = "DRIVER={%s};""server=%s;""Database=%s;""Trusted_Connection=yes" % (
#             self.maindriver, self.server, self.database)
#
#             try:
#                 self.connection = pyodbc.connect(connection_string)
#
#             except Exception as e:
#
#                 raise ConnectionError('Failed to Connect to server\n' + str(e))
#         else:
#
#             connection_string = "DRIVER={%s};""server=%s;""Database=%s;""uid=%s;""pwd=%s" % (
#             self.maindriver, self.server, self.database, self.uid, self.pwd)
#
#             try:
#                 self.connection = pyodbc.connect(connection_string)
#
#             except Exception as e:
#
#                 raise ConnectionError('Failed to Connect to server\n' + str(e))
#
#         self.connection_string = connection_string
#
#         print('Successful Connection')
#
#     def get_server_version(self):
#
#         query = '''
# 		SELECT @@VERSION
# 		'''
#         return self.execute_query(query).as_matrix()[0][0]

# @validate_arguments
# def _get_ads_odbc(type: int = AdsType().conn_type) -> str:
#     try:
#         if (type == AdsType().conn_type):
#             model = AdvanatageDataDirectory().dict()
#             # validate connection type
#             model['conn_type'] = type
#             conn_string = f"DRIVER={{{model['driver']}}};" \
#                           f"DataDirectory={model['data_directory']};" \
#                           f"SERVER={model['server']};" \
#                           f"Compression={model['сompression']};" \
#                           f"DefaultType={model['default_type']};" \
#                           f"Rows={model['rows']};" \
#                           f"Language={model['language']};" \
#                           f"AdvantageLocking={model['advantage_locking']};" \
#                           f"Locking={model['locking']};" \
#                           f"MemoBlockSize={model['memo_block_size']};" \
#                           f"MaxTableCloseCache={model['max_table_close_cache']};" \
#                           f"ServerTypes={model['server_types']};" \
#                           f"TrimTrailingSpace={model['trim_trailing_space']};" \
#                           f"UID={model['uid']};" \
#                           f"Password={model['pwd']};"
#     except ValidationError as e:
#         raise e
#
#     return conn_string
