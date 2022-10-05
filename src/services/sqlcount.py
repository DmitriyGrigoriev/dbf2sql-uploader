import logging
from src.apps.common.dataclasses import ETL
from src.services.sqllocal import SQLLocalFts

logger = logging.getLogger(__name__)


class SQLCount(SQLLocalFts):
    """Calculate record count in DBF file"""

    def __init__(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str,
                 export_database_name: str, logger: object = None,
                 mode: str = ETL.MODE.FULL
                 ) -> None:

        super(SQLCount, self).__init__(
            source_connection_name, source_table_name,
            dest_connection_name, dest_table_name,
            export_database_name, logger=logger,
            mode=mode
        )

    def count(self) -> int:
        return self._dest_model_record_count()
