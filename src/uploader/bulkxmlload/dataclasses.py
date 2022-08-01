from dataclasses import dataclass
from connection.dataclasses import FieldInfo

@dataclass
class xsdBaseType:
    field: FieldInfo

    def __init__(self, field: FieldInfo):
        self.field = field

    def xsdelement(self) -> str:
        return self._after(element=self._xsdelement())

    def _xsdelement(self):
        return ''

    def _after(self, element: str) -> str:
        return element + "\n\t\t\t\t\t\t\t"


@dataclass
class xsdTypeInteger(xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self.field.field_name}" type="xsd:int"/>"""


@dataclass
class xsdTypeChar(xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self.field.field_name}">
						<xsd:simpleType>
							<xsd:restriction base="xsd:string">
								<xsd:maxLength value="{self.field.precision}"/>
							</xsd:restriction>
						</xsd:simpleType>
					</xsd:element>"""


@dataclass
class xsdTypeCharBinary(xsdTypeChar):
    pass


@dataclass
class xsdTypeVarchar(xsdTypeChar):
    pass


@dataclass
class xsdTypeVarcharBinary(xsdTypeChar):
    pass


@dataclass
class xsdTypeDate(xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self.field.field_name}" type="xsd:date"/>"""


@dataclass
class xsdTypeDateTime(xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self.field.field_name}" type="xsd:dateTime" sql:datatype="dateTime"/>n"""


@dataclass
class xsdTypeDouble(xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self.field.field_name}" type="xsd:double"/>"""


@dataclass
class xsdTypeBoolean(xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self.field.field_name}" type="xsd:boolean"/>"""


@dataclass
class xsdTypeCurrency(xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self.field.field_name}">
						<xsd:simpleType>
							<xsd:restriction base="xsd:decimal">
								<xsd:totalDigits value="{self.field.precision}"/>
								<xsd:fractionDigits value="{self.field.scale}"/>
							</xsd:restriction>
						</xsd:simpleType>
					</xsd:element>"""


@dataclass
class xsdTypeFloat(xsdTypeCurrency):
    pass


class xsdTypeNumeric(xsdTypeCurrency):
    pass


@dataclass
class xsdTypeMemo(xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self.field.field_name}">
						<xsd:simpleType>
							<xsd:restriction base="xsd:string">
								<xsd:maxLength value="2147483647"/>
							</xsd:restriction>
						</xsd:simpleType>
					</xsd:element>"""


@dataclass
class xsdTypeMemo(xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self.field.field_name}">
						<xsd:simpleType>
							<xsd:restriction base="xsd:string">
								<xsd:maxLength value="2147483647"/>
							</xsd:restriction>
						</xsd:simpleType>
					</xsd:element>"""


@dataclass
class xsdTypeMemoBinary(xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self.field.field_name}">
						<xsd:simpleType>
							<xsd:restriction base="xsd:base64Binary">
								<xsd:maxLength value="2147483647"/>
							</xsd:restriction>
						</xsd:simpleType>
					</xsd:element>"""


@dataclass
class xsdTypeVarbinary(xsdBaseType):
    def _xsdelement(self):
        return f"""<xsd:element name="{self.field.field_name}">
						<xsd:simpleType>
							<xsd:restriction base="xsd:base64Binary">
								<xsd:maxLength value="{self.field.precision}"/>
							</xsd:restriction>
						</xsd:simpleType>
					</xsd:element>"""
