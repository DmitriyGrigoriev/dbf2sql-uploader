import logging
from datetime import datetime
from typing import Any, Dict, List

from src.config import settings
from src.services.sqlcount import RecordCount
from src.apps.common.dataclasses import ImportInfo, ETL
from src.apps.common.functions import get_last_dbf_file_modify_date, get_redis_client

logger = logging.getLogger(__name__)

def need_to_upload(record: ImportInfo, mode: str) -> bool:
    """
    If we have export from DB compare data from DBF with the time of the file which
    was saved in a table, another way compare records count in table with destination
    source

    :param record:
    :return: Bool
    """
    # https: //github.com/Bogdanp/django_dramatiq/issues/24

    redis_client = get_redis_client()
    if record.redis_message_id:
        already_in_queue: bool = redis_client.hexists(
            ETL.DRAMATIQ.DRAMATIQ_MSGS, str(record.redis_message_id)
        )
    else:
        already_in_queue = False

    # Run force export/import
    if mode == ETL.MODE.FULL:
        result = True if not already_in_queue else False
    else:
        # Task is not in Redis queue
        if not already_in_queue:
            # Compare uploaded records from source table and LocalFts destination table
            result = (
                    record.upload_record != record.table_record or record.status.title() != ETL.TASKSTATUS.DONE
            )
        else:
            result = False

    return result

def tables_import_info_list(poll_pk: int, mode: str = '') -> List[ImportInfo]:
    """
    Return list of tables which have file last write time different from imported last time

    :param poll_pk:
    :return: ImportInfo
    """

    t_rec_list: List[ImportInfo] = get_upload_record_value(poll_pk=poll_pk)

    t_list = [
        ImportInfo(
            t.table_pk,
            t.poll_pk,
            t.source_connection_name,
            t.source_table_name,
            t.dest_connection_name,
            t.dest_table_name,
            t.data_directory,
            t.type,  # import type: DBF / ARM
            t.last_write,
            t.upload_record,
            t.table_record,
            t.status,
            t.redis_message_id
        )
        for t in t_rec_list if need_to_upload(record=t, mode=mode)
    ]
    # for t in t_rec_list if mode == ETL.MODE.FULL if mode != ETL.MODE.FULL and need_to_upload(t)
    return t_list

def get_upload_record_value(poll_pk: int) -> List[ImportInfo]:
    from src.apps.core.models import ConnectSet, ImportTables

    connection_poll = ConnectSet.consets.record(pk=poll_pk)
    t_list = [
        ImportInfo(
            t.pk,
            connection_poll.pk,
            t.connects.source_conection.slug_name,
            t.source_table,
            t.connects.dest_conection.slug_name,
            t.dest_table,
            connection_poll.source_conection.name,  # DataDirectory
            connection_poll.type,  # import type: DBF / ARM
            t.last_write,
            t.upload_record,
            # Calculate count records for each table in database
            RecordCount(
                ImportInfo(
                    t.pk,
                    connection_poll.pk,
                    t.connects.source_conection.slug_name,
                    t.source_table,
                    t.connects.dest_conection.slug_name,
                    t.dest_table,
                    connection_poll.source_conection.name,  # DataDirectory
                    connection_poll.type,  # import type: DBF / ARM
                    t.last_write,
                    t.upload_record,
                    0,
                    t.message.status if t.message is not None else ETL.TASKSTATUS.UNKNOWN,
                    str(t.redis_message_id)
                ),
            ).count(),
            t.message.status if t.message is not None else ETL.TASKSTATUS.UNKNOWN,
            str(t.redis_message_id)
        )
        for t in ImportTables.tables.tables_for_import(connection_poll.pk)
    ]
    return t_list


def table_import_info(table_pk: int) -> List[ImportInfo]:
    """Fill kwargs dict by data"""
    from src.apps.core.models import ImportTables

    t = ImportTables.tables.filter(pk=table_pk).get()
    t_list = [
        ImportInfo(
            t.pk,
            t.connects.pk,
            t.connects.source_conection.slug_name,
            t.source_table,
            t.connects.dest_conection.slug_name,
            t.dest_table,
            t.dest_table,
            t.connects.type,  # import type: DBF / ARM
            t.last_write,
            t.upload_record,
            0,
            t.message.status if t.message is not None else ETL.TASKSTATUS.UNKNOWN,
            str(t.redis_message_id)
        )
    ]
    return t_list


def update_message_id(message_data: Dict[str, Any]) -> None:
    from src.apps.core.models import ImportTables

    message_id = message_data["message_id"]
    params = ImportInfo.from_dict(message_data['kwargs'])
    record_to_update = ImportTables.tables.filter(pk=params.table_pk)
    record_to_update.update(message_id=message_id)


def update_last_import_date(message_data: Dict[str, Any], result: int) -> None:
    """
    Update the date and time of last write uploaded data from the import table

    :param message_data:
    :param result:
    :return:
    """
    from src.apps.core.models import ImportTables

    databases = settings.DATABASES
    message_id = message_data["message_id"]
    params = ImportInfo.from_dict(message_data['kwargs'])
    source_databases = databases[params.source_connection_name]

    print(f"############ Message id {message_id} is success ########")

    record_to_update = ImportTables.tables.filter(pk=params.table_pk)

    if source_databases:
        data_directory = source_databases["NAME"]
        source_table = f"{params.source_table_name}"
        if params.type == ETL.EXPORT.DBF:
            # Get last write file date
            last_write = get_last_dbf_file_modify_date(
                data_directory, source_table
            )
            print(
                f"#### Success import from file {data_directory}{source_table}.DBF ####"
            )
        else:
            last_write = datetime.today()
            print(
                f"#### Success import from database {params.source_connection_name} table {source_table} ####"
            )

        if last_write:
            # last_write = datetime.fromtimestamp(last_write_time, tz=pytz.timezone(settings.TIME_ZONE)).strftime('%Y-%m-%d %H:%M:%S')
            record_to_update.update(last_write=last_write)

        if isinstance(result, int) and result is not None:
            print(f"############# {result} records has been imported #######")
            record_to_update.update(upload_record=result)
        else:
            record_to_update.update(upload_record=0)
        # Update import_table redis message id
        # update_message_id(message_data)
