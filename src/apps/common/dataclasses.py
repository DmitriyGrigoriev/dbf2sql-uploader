from datetime import datetime
from pydantic.dataclasses import dataclass

from src.config.settings import env


@dataclass
class Export:
    DBF: str = "DBF"
    DOC2SQL: str = "ARM"


@dataclass
class Mode:
    EXPORT: str = "only-export"
    IMPORT: str = "only-import"
    FULL: str = "export-import"


@dataclass
class Field:
    HASH: str = "hash"
    G07X: str = "g07x"
    G071: str = "g071"
    G072: str = "g072"
    G073: str = "g073"
    EXPTYPE: str = "sourcetype"
    DATABASE: str = "database"


@dataclass
class UrlName:
    EXPORT_SINGLE_TABLE: str = "export-from-single-table"
    PIPELINE_EXPORT_IMPORT: str = "pipeline-export-import"


@dataclass
class TimeLimit:
    ONE_HOUR: int = 3600000
    TWO_HOUR: int = 3600000 * 2
    THREE_HOUR: int = 3600000 * 3
    FOUR_HOUR: int = 3600000 * 4
    FIVE_HOUR: int = 3600000 * 5
    SIX_HOUR: int = 3600000 * 6
    SEVEN_HOUR: int = 3600000 * 7
    EIGHT_HOUR: int = 3600000 * 8
    NIGHT_HOUR: int = 3600000 * 9


@dataclass
class Connect:
    LOCALFTS: str = "localfts"


@dataclass
class Bulk:
    # BATCH_SIZE: int = 10
    BATCH_SIZE: int = 1000
    SHIFT_MONTHS: int = env.int('SHIFT_MONTHS', default=-1)


@dataclass
class PipeModules:
    DBF_EXPORT: str = "src.apps.dbfexport"
    DBF_IMPORT: str = "src.apps.sqlimport"
    DBF_RESOURCE: str = "resources"
    DBF_TABLE_PREFIX: str = "T"
    DOC2SQL_EXPORT: str = "src.apps.armexport"
    DOC2SQL_IMPORT: str = "src.apps.armimport"
    DOC2SQL_RESOURCE: str = "resources"
    DOC2SQL_TABLE_PREFIX: str = ""


@dataclass
class RedisClient:
    DRAMATIQ_MSGS: str = "dramatiq:default.msgs"
    DRAMATIQ_DQ_MSGS: str = "dramatiq:default.DQ.msgs"  # delay queue


@dataclass
class Etl:
    EXPORT: Export = Export()
    MODE: Mode = Mode()
    FIELD: Field = Field()
    URLNAME: UrlName = UrlName()
    TIMELMIT: TimeLimit = TimeLimit()
    CONNECT: Connect = Connect()
    BULK: Bulk = Bulk()
    PIPE_MODULES: PipeModules = PipeModules()
    DRAMATIQ: RedisClient = RedisClient()


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


@dataclass
class RecordInfo:
    source_connection_name: str
    source_table_name: str
    dest_connection_name: str
    dest_table_name: str
    data_directory: str
    last_write: datetime
    upload_record: int


ETL = Etl()
