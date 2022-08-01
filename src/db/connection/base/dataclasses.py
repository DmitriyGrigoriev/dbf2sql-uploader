from dataclasses import dataclass


@dataclass
class FieldInfo:
    table: str
    field_name: str
    field_type: str
    precision: int
    scale: int
    nullable: bool
    default: str

"""
Each row fetched has the following columns:
         0) table_cat: The catalog name.
         1) table_schem: The schema name.
         2) table_name: The table name.
         3) table_type: One of 'TABLE', 'VIEW', SYSTEM TABLE', 'GLOBAL TEMPORARY'
            'LOCAL TEMPORARY', 'ALIAS', 'SYNONYM', or a data source-specific type name.
"""
@dataclass
class TableInfo:
    table_cat: str
    table_schem: str
    table_name: str
    table_type: str
