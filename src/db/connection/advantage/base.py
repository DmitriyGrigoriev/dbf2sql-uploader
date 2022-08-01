from django.core.exceptions import ImproperlyConfigured
from django.utils.encoding import smart_str  # noqa

try:
    import pyodbc as Database
except ImportError as e:
    raise ImproperlyConfigured("Error loading pyodbc module: %s" % e)

from django.db.backends.base.base import BaseDatabaseWrapper
from .schema import DatabaseSchemaEditor
from .introspection import DatabaseIntrospection
from .client import DatabaseClient
from .creation import DatabaseCreation
from .features import DatabaseFeatures  # noqa
from .operations import DatabaseOperations


def encode_connection_string(fields):
    """Encode dictionary of keys and values as an ODBC connection String.

    See [MS-ODBCSTR] document:
    https://msdn.microsoft.com/en-us/library/ee208909%28v=sql.105%29.aspx
    """
    # As the keys are all provided by us, don't need to encode them as we know
    # they are ok.
    return ';'.join(
        '%s=%s' % (k, encode_value(v))
        for k, v in fields.items()
    )


def encode_value(v):
    """If the value contains a semicolon, or starts with a left curly brace,
    then enclose it in curly braces and escape all right curly braces.
    """
    if ';' in v or v.strip(' ').startswith('{'):
        return '{%s}' % (v.replace('}', '}}'),)
    return v


class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = "None"
    display_name = "Advantage StreamlineSQL"
    # SQLite doesn't actually support most of these types, but it "does the right
    # thing" given more verbose field definitions, so leave them as is so that
    # schema inspection is more useful.
    data_types = {
        "AutoField": "autoinc",
        "IntegerField": "integer",
        "CharField": "char(%(max_length)s)",
        "DateField": "date",
        "DateTimeField": "timestamp",
        "FloatField": "float",
        "FloatField": "double",
        "TextField": "memo",
        "BooleanField": "logical",
        "IPAddressField": "char(15)",
        "GenericIPAddressField": "char(39)",
        "JSONField": "memo",
        "PositiveIntegerField": "integer",
        "SlugField": "varchar(%(max_length)s)",
        "SmallIntegerField": "integer",
        "UUIDField": "char(32)",
        "DecimalField": "numeric(%(max_digits)s, %(decimal_places)s)",
        "BinaryField": "varbinary(%(max_length)s)",
        # "DurationField": "int",
        # "BigAutoField": "autoinc",
        # "SmallAutoField": "autoinc",
        # "PositiveSmallIntegerField": "integer",
        # "OneToOneField": "integer",
        # "PositiveBigIntegerField": "integer",
        # "FileField": "varchar(%(max_length)s)",
        # "FilePathField": "varchar(%(max_length)s)",
        # "BigIntegerField": "int",
        # "TimeField": "char(8)",
    }
    operators = {
        # Since '=' is used not only for string comparision there is no way
        # to make it case (in)sensitive.
        'exact': '= %s',
        'iexact': "= UPPER(%s)",
        'contains': "LIKE %s ESCAPE '\\'",
        'icontains': "LIKE UPPER(%s) ESCAPE '\\'",
        'gt': '> %s',
        'gte': '>= %s',
        'lt': '< %s',
        'lte': '<= %s',
        'startswith': "LIKE %s ESCAPE '\\'",
        'endswith': "LIKE %s ESCAPE '\\'",
        'istartswith': "LIKE UPPER(%s) ESCAPE '\\'",
        'iendswith': "LIKE UPPER(%s) ESCAPE '\\'",
    }
    data_types_suffix = {
        'AutoField': 'NEXTVALUE 1, STEP 1',
        'BigAutoField': 'NEXTVALUE 1, STEP 1',
        'SmallAutoField': 'NEXTVALUE 1, STEP 1',
    }
    data_type_check_constraints = {
        'JSONField': '(ISJSON ("%(column)s") = 1)',
        'PositiveIntegerField': '[%(column)s] >= 0',
        'PositiveSmallIntegerField': '[%(column)s] >= 0',
        'PositiveBigIntegerField': '[%(column)s] >= 0',
    }
    # The patterns below are used to generate SQL pattern lookup clauses when
    # the right-hand side of the lookup isn't a raw string (it might be an expression
    # or the result of a bilateral transformation).
    # In those cases, special characters for LIKE operators (e.g. \, *, _) should be
    # escaped on database side.
    #
    # Note: we use str.format() here for readability as '%' is used as a wildcard for
    # the LIKE operator.
    pattern_esc = r"REPLACE(REPLACE(REPLACE({}, '\', '\\'), '%%', '\%%'), '_', '\_')"
    pattern_ops = {
        "contains": r"LIKE '%%' || {} || '%%' ESCAPE '\'",
        "icontains": r"LIKE '%%' || UPPER({}) || '%%' ESCAPE '\'",
        "startswith": r"LIKE {} || '%%' ESCAPE '\'",
        "istartswith": r"LIKE UPPER({}) || '%%' ESCAPE '\'",
        "endswith": r"LIKE '%%' || {} ESCAPE '\'",
        "iendswith": r"LIKE '%%' || UPPER({}) ESCAPE '\'",
    }
    Database = Database
    SchemaEditorClass = DatabaseSchemaEditor
    # Classes instantiated in __init__().
    client_class = DatabaseClient
    creation_class = DatabaseCreation
    features_class = DatabaseFeatures
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations

    _codes_for_networkerror = (
        '08S01',
        '08S02',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # opts = self.settings_dict["OPTIONS"]

        # capability for multiple result sets or cursors
        self.supports_mars = False

    def get_connection_params(self):
        settings_dict = self.settings_dict
        if not settings_dict["NAME"]:
            raise ImproperlyConfigured(
                "settings.DATABASES is improperly configured. "
                "Please supply the NAME value."
            )
        conn_params = settings_dict.copy()
        # kwargs = {
        #     "database": settings_dict["NAME"],
        #     **settings_dict["OPTIONS"],
        # }
        return conn_params


    def get_new_connection(self, conn_params):
        database = conn_params['NAME']
        user = conn_params.get('USER', None)
        password = conn_params.get('PASSWORD', None)
        # port = conn_params.get('PORT', None)
        # trusted_connection = conn_params.get('Trusted_Connection', 'yes')

        options = conn_params.get('OPTIONS', {})
        driver = options.get('driver', 'Advantage StreamlineSQL ODBC')
        dsn = options.get('dsn', None)
        options_extra_params = options.get('extra_params', '')

        cstr_parts = {}
        if dsn:
            cstr_parts['DSN'] = dsn
        else:
            # Only append DRIVER if DATABASE_ODBC_DSN hasn't been set
            cstr_parts['DRIVER'] = driver

        cstr_parts['SERVER'] = 'NotTheServer'
        cstr_parts['DefaultType'] = 'Clipper'
        cstr_parts['AdvantageLocking'] = 'OFF'
        cstr_parts['Locking'] = 'Record'
        cstr_parts['MemoBlockSize'] = '64'
        cstr_parts['TrimTrailingSpace'] = 'True'

            # if ms_drivers.match(driver):
            #     if port:
            #         host = ','.join((host, str(port)))
            #     cstr_parts['SERVER'] = host
            # elif options.get('host_is_server', False):
            #     if port:
            #         cstr_parts['PORT'] = str(port)
            #     cstr_parts['SERVER'] = host
            # else:
            #     cstr_parts['SERVERNAME'] = host

        if user:
            cstr_parts['UID'] = user
            cstr_parts['PWD'] = password
            # if 'Authentication=ActiveDirectoryInteractive' not in options_extra_params:
            #     cstr_parts['PWD'] = password
        # elif 'TOKEN' not in conn_params:
        #     if ms_drivers.match(driver) and 'Authentication=ActiveDirectoryMsi' not in options_extra_params:
        #         cstr_parts['Trusted_Connection'] = trusted_connection
        #     else:
        #         cstr_parts['Integrated Security'] = 'SSPI'

        cstr_parts['DataDirectory'] = database

        # if ms_drivers.match(driver) and os.name == 'nt':
        #     cstr_parts['MARS_Connection'] = 'yes'
        #
        connstr = encode_connection_string(cstr_parts)

        # extra_params are glued on the end of the string without encoding,
        # so it's up to the settings writer to make sure they're appropriate -
        # use encode_connection_string if constructing from external input.
        if options.get('extra_params', None):
            connstr += ';' + options['extra_params']

        # unicode_results = options.get('unicode_results', False)
        # timeout = options.get('connection_timeout', 0)
        # retries = options.get('connection_retries', 5)
        # backoff_time = options.get('connection_retry_backoff_time', 5)
        # query_timeout = options.get('query_timeout', 0)
        setencoding = options.get('setencoding', None)
        setdecoding = options.get('setdecoding', None)

        conn = None
        # retry_count = 0
        need_to_retry = False
        if setdecoding:
            args = {
                'ansi': True,
            }
        else:
            args = {}

        while conn is None:
            try:
                conn = Database.connect(connstr, **args)
            except Exception as e:
                # for error_number in self._transient_error_numbers:
                #     if error_number in e.args[1]:
                #         if error_number in e.args[1] and retry_count < retries:
                #             time.sleep(backoff_time)
                #             need_to_retry = True
                #             retry_count = retry_count + 1
                #         else:
                #             need_to_retry = False
                #         break
                if not need_to_retry:
                    raise

        # conn.timeout = query_timeout
        if setencoding:
            conn.setencoding(**setencoding)
            # for entry in setencoding:
            #     conn.setencoding(**entry)
        if setdecoding:
            conn.setdecoding(Database.SQL_CHAR, **setdecoding)
            # for entry in setdecoding:
            #     conn.setdecoding(**entry)
        return conn


    def _set_autocommit(self, autocommit):
        # AUTO COMMIT MODE:
        # In auto commit mode (the default transaction processing mode),
        # the Advantage ODBC Driver does not use transactions when making
        # updates to the data.
        # If you do want every statement to run in an individual transaction,
        # you can use the SQL statement SET TRANSACTION to turn on autocommit
        # state at the server.
        pass


    def init_connection_state(self):
        pass


    def is_usable(self):
        try:
            self.create_cursor().execute("SELECT TOP 1 * FROM system.tables;")
        except Database.Error:
            return False
        else:
            return True


    def create_cursor(self, name=None):
        return CursorWrapper(self.connection.cursor(), self)


    def _on_error(self, e):
        if e.args[0] in self._codes_for_networkerror:
            try:
                # close the stale connection
                self.close()
                # wait a moment for recovery from network error
                # time.sleep(self.connection_recovery_interval_msec)
            except Exception:
                pass
            self.connection = None


class CursorWrapper(object):
    """
    A wrapper around the pyodbc's cursor that takes in account a) some pyodbc
    DB-API 2.0 implementation and b) some common ODBC driver particularities.
    """

    def __init__(self, cursor, connection):
        self.active = True
        self.cursor = cursor
        self.connection = connection
        # self.driver_charset = connection.driver_charset
        self.last_sql = ''
        self.last_params = ()

    def close(self):
        if self.active:
            self.active = False
            self.cursor.close()

    def format_sql(self, sql, params):
        # if self.driver_charset and isinstance(sql, str):
        #     # FreeTDS (and other ODBC drivers?) doesn't support Unicode
        #     # yet, so we need to encode the SQL clause itself in utf-8
        #     sql = smart_str(sql, self.driver_charset)

        # pyodbc uses '?' instead of '%s' as parameter placeholder.
        if params is not None:
            sql = sql % tuple('?' * len(params))

        return sql

    def format_params(self, params):
        fp = []
        if params is not None:
            for p in params:
                if isinstance(p, str):
                    fp.append(p)
                    # if self.driver_charset:
                    #     # FreeTDS (and other ODBC drivers?) doesn't support Unicode
                    #     # yet, so we need to encode parameters in utf-8
                    #     fp.append(smart_str(p, self.driver_charset))
                    # else:
                    #     fp.append(p)

                elif isinstance(p, bytes):
                    fp.append(p)

                elif isinstance(p, type(True)):
                    if p:
                        fp.append(1)
                    else:
                        fp.append(0)

                else:
                    fp.append(p)

        return tuple(fp)

    def execute(self, sql, params=None):
        self.last_sql = sql
        sql = self.format_sql(sql, params)
        params = self.format_params(params)
        self.last_params = params
        try:
            return self.cursor.execute(sql, params)
        except Database.Error as e:
            self.connection._on_error(e)
            raise

    def executemany(self, sql, params_list=()):
        if not params_list:
            return None
        raw_pll = [p for p in params_list]
        sql = self.format_sql(sql, raw_pll[0])
        params_list = [self.format_params(p) for p in raw_pll]
        try:
            return self.cursor.executemany(sql, params_list)
        except Database.Error as e:
            self.connection._on_error(e)
            raise

    def format_rows(self, rows):
        return list(map(self.format_row, rows))

    def format_row(self, row):
        """
        Decode data coming from the database if needed and convert rows to tuples
        (pyodbc Rows are not hashable).
        """
        # if self.driver_charset:
        #     for i in range(len(row)):
        #         f = row[i]
        #         # FreeTDS (and other ODBC drivers?) doesn't support Unicode
        #         # yet, so we need to decode utf-8 data coming from the DB
        #         if isinstance(f, bytes):
        #             row[i] = f.decode(self.driver_charset)
        return tuple(row)

    def fetchone(self):
        row = self.cursor.fetchone()
        if row is not None:
            row = self.format_row(row)
        # Any remaining rows in the current set must be discarded
        # before changing autocommit mode when you use FreeTDS
        if not self.connection.supports_mars:
            self.cursor.nextset()
        return row

    def fetchmany(self, chunk):
        return self.format_rows(self.cursor.fetchmany(chunk))

    def fetchall(self):
        return self.format_rows(self.cursor.fetchall())

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]
        return getattr(self.cursor, attr)

    def __iter__(self):
        return iter(self.cursor)
