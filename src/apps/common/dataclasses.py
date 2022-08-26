from dataclasses import dataclass
from datetime import datetime

@dataclass
class ImportInfo:
    table_pk: int
    poll_pk: int
    source_connection_name: str
    source_table_name: str
    dest_connection_name: str
    dest_table_name: str
    data_directory: str
    type: str

