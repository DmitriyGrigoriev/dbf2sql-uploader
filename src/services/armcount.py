import logging
import datetime
from src.apps.common.dataclasses import ETL
from src.services.armimport import ARMImport

logger = logging.getLogger(__name__)

class ARMCount(ARMImport):

    def __init__(self, source_connection_name: str, source_table_name: str,
                 dest_connection_name: str, dest_table_name: str, logger=None,
                 mode: str = ETL.MODE.FULL
                 ) -> int:

        super(ARMCount, self).__init__(
            source_connection_name, source_table_name,
            dest_connection_name, dest_table_name, logger=logger,
            mode=mode
        )

    def count(self) -> int:
        try:
            self._reccount = self._source_model_record_count()

        except Exception as e:
            if self.logger:
                self.logger.error(e)
            else:
                logger.exception(e)
            raise e

        return self._reccount