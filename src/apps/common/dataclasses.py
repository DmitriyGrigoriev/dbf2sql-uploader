from datetime import datetime
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from django.utils.translation import gettext_lazy as _
from marshmallow import fields

from src.config.env import env

@dataclass_json
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
    last_write: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso')
        )
    )
    upload_record: int
    table_record: int
    status: str
    redis_message_id: str
    # redis_message_id: UUID = field(default_factory=uuid4)

@dataclass(frozen=True)
class Export:
    DBF: str = "DBF"
    DOC2SQL: str = "ARM"
    NSI: str = "NSI"

@dataclass(frozen=True)
class Mode:
    EXPORT: str = "only-export"
    IMPORT: str = "only-import"
    FULL: str = "export-import"


@dataclass(frozen=True)
class Field:
    HASH: str = "hash"
    G07X: str = "g07x"
    G071: str = "g071"
    G072: str = "g072"
    G073: str = "g073"
    G021: str = "g021"
    G022: str = "g022"
    G027: str = "g027"
    G081: str = "g081"
    G082: str = "g082"
    G087: str = "g087"
    G141: str = "g141"
    G142: str = "g142"
    G147: str = "g147"
    G011: str = "g011"
    GD0: str = "gd0"
    EXPTYPE: str = "sourcetype"
    DATABASE: str = "database"

@dataclass(frozen=True)
class MainTables:
    DCLHEAD: str = "dclhead"
    DCLTOVAR: str = "dcltovar"
    DCLTECHD: str = "dcltechd"

@dataclass(frozen=True)
class UrlName:
    EXPORT_SINGLE_TABLE: str = "export-from-single-table"
    PIPELINE_EXPORT_IMPORT: str = "pipeline-export-import"

@dataclass(frozen=True)
class TaskStatus:
    ENDQUEUED = _("Enqueued")
    DELAYED = _("Delayed")
    RUNNING = _("Running")
    FAILED = _("Failed")
    DONE = _("Done")
    SKIPPED = _("Skipped")
    UNKNOWN = _("Unknown")


@dataclass(frozen=True)
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


@dataclass(frozen=True)
class Connect:
    LOCALFTS: str = "localfts"
    NAVISION: str = "nav"


@dataclass
class Bulk:
    # BATCH_SIZE: int = 100
    BATCH_SIZE: int = 1000
    BATCH_SLICE: int = 20000
    SHIFT_MONTHS: int = env.int('SHIFT_MONTHS', default=-2)


@dataclass(frozen=True)
class PipeModules:
    DBF_EXPORT: str = "src.apps.dbfexport"
    DBF_IMPORT: str = "src.apps.sqlimport"
    DBF_RESOURCE: str = "resources"
    DBF_TABLE_PREFIX: str = "T"
    DOC2SQL_EXPORT: str = "src.apps.armexport"
    DOC2SQL_IMPORT: str = "src.apps.armimport"
    DOC2SQL_RESOURCE: str = "resources"
    DOC2SQL_TABLE_PREFIX: str = ""
    NSI_EXPORT: str = "src.apps.nsiexport"
    NSI_IMPORT: str = "src.apps.nsimport"
    NSI_RESOURCE: str = "resources"
    NSI_TABLE_PREFIX: str = ""


@dataclass(frozen=True)
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
    MAINTABLES: MainTables = MainTables()
    TASKSTATUS: TaskStatus = TaskStatus()


ETL = Etl()