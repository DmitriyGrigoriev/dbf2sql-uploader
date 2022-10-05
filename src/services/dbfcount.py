import logging
from src.apps.common.dataclasses import ETL
from src.services.sqlimport import SQLImport

logger = logging.getLogger(__name__)


class DBFCount(SQLImport):
    """Calculate record count in DBF file"""

    def __init__(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str, logger: object = None,
                 mode: str = ETL.MODE.FULL
                 ) -> None:

        super(DBFCount, self).__init__(
            source_connection_name, source_table_name,
            dest_connection_name, dest_table_name, logger=logger,
            mode=mode
        )

    def count(self) -> int:
        return self._source_model_record_count()
