import math
import datetime
from connection.dataclasses import FieldInfo
from .dataclasses import xsdTypeChar, xsdTypeDate, xsdTypeBoolean, xsdTypeNumeric

class XSDSchema:

    def __init__(self, connection: object, t_sql: str, table: str):
        self.connection = connection
        self.t_sql = t_sql
        self.table_name = table
        self.fields = self.get_fields_description()


    def get_fields_description(self) -> dict:
        """Returns a description of the sql columns, with the DB-API cursor.description interface."""
        cursor = self.connection.cursor().execute(self.t_sql).description
        table: str = self.table_name
        return {
            f[0]:
            FieldInfo(
                table=table.lower(),
                field_name=f[0],
                field_type=self._get_field_type(typeof=f[1]),
                precision=f[4],
                scale=f[5],
                nullable=bool(f[6]),
                default=None
            ) for f in cursor
        }

    def _get_field_type(self, typeof: object):
        field_type: str = ''
        if typeof == datetime.date:
            field_type: str = 'DATE'
        elif typeof == datetime.datetime:
            field_type: str = 'DATETIME'
        elif typeof == str:
            field_type: str = 'CHAR'
        elif typeof == int:
            field_type: str = 'INTEGER'
        elif typeof == bool:
            field_type: str = 'LOGICAL'
        elif typeof == float:
            floor_value: int = math.floor(typeof)
            ceil_value: int = math.ceil(typeof)
            value_size: int = len(str(floor_value) + str(ceil_value))
            if value_size < 19 and ceil_value == 4:
                field_type = 'CURRENCY'
            elif value_size < 19:
                field_type: str = 'NUMERIC'
            else:
                field_type: str = 'FLOAT'
        else:
            raise ValueError("Unexpectable field type")
        return field_type

    def schema(self) -> str:
        fields: dict = self.fields
        table_name: str = self.table_name
        sequence:str = ''
        for f in fields.keys():
            field = fields[f]
            if (field.field_type == 'CHAR'):
                sequence = sequence + xsdTypeChar(field=field).xsdelement()
            elif (field.field_type == 'DATE'):
                sequence = sequence + xsdTypeDate(field=field).xsdelement()
            elif (field.field_type == 'NUMERIC'):
                sequence = sequence + xsdTypeNumeric(field=field).xsdelement()
            elif (field.field_type == 'LOGICAL'):
                sequence = sequence + xsdTypeBoolean(field=field).xsdelement()
            else:
                raise ValueError("Unexpectable xsd field type")

        return f"""<?xml version = "1.0" encoding="utf-8" standalone="yes"?>
        <xsd:schema id="NTXData" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata" xmlns:sql="urn:schemas-microsoft-com:mapping-schema">
        	<xsd:element name="NTXData" msdata:IsDataSet="true" sql:is-constant="1">
        		<xsd:complexType>
        			<xsd:sequence>
        				<xsd:element name="{table_name}" sql:relation="{table_name}" minOccurs="0" maxOccurs="unbounded">
        					<xsd:complexType>
        						<xsd:sequence>
                                    {sequence}</xsd:sequence>
        					</xsd:complexType>
        				</xsd:element>
        			</xsd:sequence>
        			<xsd:anyAttribute namespace="http://www.w3.org/XML/1998/namespace" processContents="lax"/>
        		</xsd:complexType>
        	</xsd:element>
        </xsd:schema>
        """
