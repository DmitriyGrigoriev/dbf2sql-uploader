# import logging
from src.services.sqllocal import SQLLocalFts
from src.services.base.baseimport import BaseImport
from src.apps.common.dataclasses import ETL, ImportInfo
# logger = logging.getLogger(__name__)


class SQLCount(SQLLocalFts):
    """Calculate record count in DBF file"""
    def __init__(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str,
                 export_database_name: str,
                 # logger: object = None,
                 # mode: str = ETL.MODE.FULL
                 ) -> None:

        super(SQLCount, self).__init__(
            source_connection_name, source_table_name,
            dest_connection_name, dest_table_name,
            export_database_name
        )

    def count(self) -> int:
        return self._dest_model_record_count()


class RecordCount(BaseImport):
    def __init__(self, params: ImportInfo) -> None:
        super(RecordCount, self).__init__(params)

    def count(self) -> int:
        """Calculate records count for DBF file"""
        if self.type == ETL.EXPORT.DBF:
            return self.dbf_record_count()
        elif self.type == ETL.EXPORT.DOC2SQL:
            return self.arm_record_count()
        else:
            raise ValueError(f"Unresolved record type, must be only {ETL.EXPORT.DBF} or {ETL.EXPORT.DOC2SQL}")
