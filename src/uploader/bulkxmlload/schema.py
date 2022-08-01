from dataclasses import dataclass
# from connection.tables import _AdsField, _AdsTable


@dataclass
class _xsdBaseType:
    # _field: _AdsField

    def __init__(self, _field: _AdsField):
        self.field = _field

    def xsdelement(self) -> str:
        return self._after(element=self._xsdelement())

    def _xsdelement(self):
        return ''

    def _after(self, element: str) -> str:
        return element + "\n\t\t\t\t\t\t\t"

@dataclass
class _xsdTypeInteger(_xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self._field.columnname}" type="xsd:int"/>"""


@dataclass
class _xsdTypeChar(_xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self._field.columnname}">
						<xsd:simpleType>
							<xsd:restriction base="xsd:string">
								<xsd:maxLength value="{self._field.precision}"/>
							</xsd:restriction>
						</xsd:simpleType>
					</xsd:element>"""


@dataclass
class _xsdTypeCharBinary(_xsdTypeChar):
    pass


@dataclass
class _xsdTypeVarchar(_xsdTypeChar):
    pass


@dataclass
class _xsdTypeVarcharBinary(_xsdTypeChar):
    pass


@dataclass
class _xsdTypeDate(_xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self._field.columnname}" type="xsd:date"/>"""


@dataclass
class _xsdTypeDateTime(_xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self._field.columnname}" type="xsd:dateTime" sql:datatype="dateTime"/>n"""


@dataclass
class _xsdTypeDouble(_xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self._field.columnname}" type="xsd:double"/>"""


@dataclass
class _xsdTypeBoolean(_xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self._field.columnname}" type="xsd:boolean"/>"""


@dataclass
class _xsdTypeCurrency(_xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self._field.columnname}">
						<xsd:simpleType>
							<xsd:restriction base="xsd:decimal">
								<xsd:totalDigits value="{self._field.precision}"/>
								<xsd:fractionDigits value="{self._field.scale}"/>
							</xsd:restriction>
						</xsd:simpleType>
					</xsd:element>"""


@dataclass
class _xsdTypeFloat(_xsdTypeCurrency):
    pass


class _xsdTypeNumeric(_xsdTypeCurrency):
    pass


@dataclass
class _xsdTypeMemo(_xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self._field.columnname}">
						<xsd:simpleType>
							<xsd:restriction base="xsd:string">
								<xsd:maxLength value="2147483647"/>
							</xsd:restriction>
						</xsd:simpleType>
					</xsd:element>"""


@dataclass
class _xsdTypeMemo(_xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self._field.columnname}">
						<xsd:simpleType>
							<xsd:restriction base="xsd:string">
								<xsd:maxLength value="2147483647"/>
							</xsd:restriction>
						</xsd:simpleType>
					</xsd:element>"""


@dataclass
class _xsdTypeMemoBinary(_xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self._field.columnname}">
						<xsd:simpleType>
							<xsd:restriction base="xsd:base64Binary">
								<xsd:maxLength value="2147483647"/>
							</xsd:restriction>
						</xsd:simpleType>
					</xsd:element>"""


@dataclass
class _xsdTypeVarbinary(_xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self._field.columnname}">
						<xsd:simpleType>
							<xsd:restriction base="xsd:base64Binary">
								<xsd:maxLength value="{self._field.precision}"/>
							</xsd:restriction>
						</xsd:simpleType>
					</xsd:element>"""


@dataclass
class XSDSchema:
    _table: _AdsTable
    _xsdelements: str

    def __init__(self, table: _AdsTable):
        self._table = table
        self._xsdelements = self._retrieve_elements(fields=self._table.fields)

    def _retrieve_elements(self, fields: _AdsField):
        element = ''
        for f in fields.keys():
            if (fields[f].typename == 'CHAR'):
                element = element + _xsdTypeChar(_field=fields[f]).xsdelement()
            elif (fields[f].typename == 'DATE'):
                element = element + _xsdTypeDate(_field=fields[f]).xsdelement()
            elif (fields[f].typename == 'NUMERIC'):
                element = element + _xsdTypeNumeric(_field=fields[f]).xsdelement()
            elif (fields[f].typename == 'LOGICAL'):
                element = element + _xsdTypeBoolean(_field=fields[f]).xsdelement()
            else:
                raise ValueError("Unexpectable xsd field type")

        return element

    def retrieve_schema(self):
        return f"""<?xml version = "1.0" encoding="utf-8" standalone="yes"?>
<xsd:schema id="NTXData" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata" xmlns:sql="urn:schemas-microsoft-com:mapping-schema">
	<xsd:element name="NTXData" msdata:IsDataSet="true" sql:is-constant="1">
		<xsd:complexType>
			<xsd:sequence>
				<xsd:element name="{self._table.tablename}" sql:relation="{self._table.tablename}" minOccurs="0" maxOccurs="unbounded">
					<xsd:complexType>
						<xsd:sequence>
                            {self._xsdelements}</xsd:sequence>
					</xsd:complexType>
				</xsd:element>
			</xsd:sequence>
			<xsd:anyAttribute namespace="http://www.w3.org/XML/1998/namespace" processContents="lax"/>
		</xsd:complexType>
	</xsd:element>
</xsd:schema>
"""
