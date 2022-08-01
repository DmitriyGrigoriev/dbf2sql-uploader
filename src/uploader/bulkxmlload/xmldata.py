import pyodbc
from dataclasses import dataclass
from connection.tables import _AdsField, _AdsTable


@dataclass
class _xmlBaseType:
    _field: _AdsField

    def __init__(self, _field: _AdsField):
        self.field = _field

    def xmlelement(self) -> str:
        return self._after(element=self._xmlelement())

    def _xmlelement(self):
        return ''

    def _after(self, element: str) -> str:
        return element + "\n"


@dataclass
class XMLData:
    _table: _AdsTable
    _xmlelements: str
    _conn: str

    def __init__(self, table: _AdsTable, conn_string: str):
        self._table = table
        self._conn = self._connect(conn_string=conn_string)
        # self._xmlelements = self._retrieve_elements(fields=self._table.fields)

    def _connect(self, conn_string: str):
        connection = pyodbc.connect(conn_string)
        return connection

    # def _retrieve_elements(self, row:pyodbc.Row):
    #     xmlrows: str = ''
    #     fields = [field[0] for field in row.cursor_description]
    #     for f in fields:
    #         xmlrows = xmlrows + f"<{f.lower()}>{getattr(row,f)}<{f.lower()}/>\n"
    #     return xmlrows

    def _retrieve_data(self):
        tables = self._conn.cursor()
        tsql = f"""SELECT * FROM {self._table.tablename} WHERE G073 = '3002512';"""
        xmlrows: str = ''
        with tables.execute(tsql):
            cursor = tables.fetchone()
            if cursor is not None:
                fields = [field[0] for field in cursor.cursor_description]
                for f in fields:
                    xmlrows = xmlrows + f"<{f.lower()}>{getattr(cursor, f)}<{f.lower()}/>\n"
        return xmlrows


    def retrieve_schema(self):
        return f"""<?xml version = "1.0" encoding="utf-8" standalone="yes"?>
<NTXData xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="{self._table.tablename.lower()}.xsd">
    <{self._table.tablename.lower()}>        
    	{self._retrieve_data()}
    </{self._table.tablename.lower()}>
</NTXData>"""

