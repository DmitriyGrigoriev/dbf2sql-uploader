from django.db.backends.base.introspection import (
    BaseDatabaseIntrospection, FieldInfo, TableInfo,
)

class FlexibleFieldLookupDict:
    # Maps SQL types to FoxPro Field types. Some of the SQL types have multiple
    # entries here because SQLite allows for anything and doesn't normalize the
    # field type; it uses whatever was given.
    base_data_types_reverse = {
        'autoinc': "AutoField",         # AUTOINC
        'integer': "IntegerField",      # INTEGER
        'char': "CharField",            # CHAR CHARBINARY
        'date': "DateField",            # DATE
        'timestamp': "DateTimeField",   # DATETIME
        'double': "FloatField",         # DOUBLE
        'float': "DecimalField",        # FLOAT
        'numeric': "DecimalField",      # NUMERIC
        'logical': "BooleanField",      # LOGICAl
        'memo': 'TextField',            # MEMO MEMOBINARY
        'binary': "FileField",          # GENERAL
        'money': 'DecimalField',        # CURRENCY
        'varbinaryfox': "BinaryField",  # VARBINARY
        'varcharfox': "CharField",      # VARCHAR VARCHARBINARY
    }

    def __getitem__(self, key):
        key = key.lower().split("(", 1)[0].strip()
        return self.base_data_types_reverse[key]


class DatabaseIntrospection(BaseDatabaseIntrospection):
    data_types_reverse = FlexibleFieldLookupDict()

    def get_table_list(self, cursor):
        """Return a list of table and view names in the current database."""
        # Skip the sqlite_sequence system table used for autoincrement key
        # generation.
        return [TableInfo(row[2].lower(), row[3][0].lower()) for row in cursor.tables().fetchall()]


    def table_names(self, cursor=None, include_views=False):
        """
        Return a list of names of all tables that exist in the database.
        Sort the returned table list by Python's default sorting. Do NOT use
        the database's ORDER BY here to avoid subtle differences in sorting
        order between databases.
        """

        def get_names(cursor):
            return sorted(
                ti.name
                for ti in self.get_table_list(cursor)
                if include_views or ti.type == "t"
            )

        if cursor is None:
            with self.connection.cursor() as cursor:
                return get_names(cursor)
        return get_names(cursor)


    def get_table_description(self, cursor, table_name):
        """
        Return a description of the table with the DB-API cursor.description
        interface.
        """
        table_info = cursor.columns(table=table_name).fetchall()
        # Creates a results set of column names in specified tables by executing the ODBC SQLColumns function.
        # Each row fetched has the following columns:
        #   0) table_cat
        #   1) table_schem
        #   2) table_name
        #   3) column_name
        #   4) data_type
        #   5) type_name
        #   6) column_size
        #   7) buffer_length
        #   8) decimal_digits
        #   9) num_prec_radix
        #  10) nullable
        #  11) remarks
        #  12) column_def
        #  13) sql_data_type
        #  14) sql_datetime_sub
        #  15) char_octet_length
        #  16) ordinal_position
        #  17) is_nullable
        return [
            # "name type_code display_size internal_size precision scale null_ok "
            # "default collation",
            FieldInfo(
                column_name.lower(),
                localtypename,      # CHAR, INTEGER ...
                None,
                buffer_length,  # internal size
                column_size  if decimal_digits == 0 else column_size + 1,
                decimal_digits,
                bool(is_nullable),
                column_def,
                None
            )
            for table_cat, \
                table_schem, \
                table_name, \
                column_name, \
                data_type, \
                type_name, \
                column_size, \
                buffer_length, \
                decimal_digits, \
                num_prec_radix, \
                nullable, \
                remarks, \
                column_def, \
                sql_data_type, \
                sql_datetime_sub, \
                char_octet_length, \
                ordinal_position, \
                is_nullable, \
                nocptrans, \
                localtypename
            in table_info
        ]


    def get_primary_key_column(self, cursor, table_name):
        """Return the column name of the primary key for the given table."""
        # Don't use PRAGMA because that causes issues with some transactions
        row = cursor.primaryKeys(table=table_name).fetchone()
        if row is None:
            return ['id']
            raise ValueError("Table %s does not exist" % table_name)

        return row[3].lower() if row[3].lower() else None
