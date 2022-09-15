import logging
from datetime import datetime

from src.config import settings
from src.apps.common.dataclasses import ETL
from src.apps.common.functions import get_last_dbf_file_modify_date, get_redis_client
from src.apps.common.dataclasses import ImportInfo, RecordInfo
from src.services.armcount import ARMCount

logger = logging.getLogger(__name__)


def need_to_upload(
        data_directory: str,
        table_name: str,
        type: str,
        last_write: datetime,
        upload_record: int,
        redis_message_id,
        record: list
) -> bool:
    """
    If we have export from DB compare data from DBF with the time of the file which
    was saved in a table, another way compare records count in table with destination
    source

    :param data_directory:
    :param table_name:
    :param type:
    :param last_write:
    :param upload_record:
    :return: Bool
    """
    redis_client = get_redis_client()
    if redis_message_id:
        already_in_queue: bool = redis_client.hexists(ETL.DRAMATIQ.DRAMATIQ_MSGS, str(redis_message_id))
    else:
        already_in_queue: bool = False

    # Task is not in Redis queue
    if not already_in_queue:
        if type == ETL.EXPORT.DBF:
            result = last_write != get_last_dbf_file_modify_date(data_directory, table_name)
        else:
            result = upload_record != [t.upload_record for t in record if
                                       t.source_table_name.lower() == table_name.lower()
                                       ]
    else:
        result = False

    return result


def tables_import_info_list(poll_pk) -> ImportInfo:
    """
    Return list of tables which have file last write time different from imported last time

    :param poll_pk:
    :return ImportInfo:
    -----------------------------
    table_pk: int
    poll_pk: int
    source_connection_name: str
    source_table_name: str
    dest_connection_name: str
    dest_table_name: str
    data_directory: str
    type: str
    ------------------------------
    """
    from src.apps.core.models import ConnectSet, ImportTables

    connection_poll = ConnectSet.consets.record(pk=poll_pk)
    source_connection_name = connection_poll.source_conection.slug_name
    dest_connection_name = connection_poll.dest_conection.slug_name

    if connection_poll.type == ETL.EXPORT.DOC2SQL:
        t_arm_list = get_upload_record(poll_pk=poll_pk)
    else:
        t_arm_list = []

    t_list = [
        ImportInfo(
            t.pk,
            connection_poll.pk,
            source_connection_name,
            t.source_table,
            dest_connection_name,
            t.dest_table,
            connection_poll.source_conection.name,  # DataDirectory
            connection_poll.type,  # import type: DBF / ARM
        )
        for t in ImportTables.tables.tables_for_import(connection_poll.pk) \
        if need_to_upload(
            connection_poll.source_conection.name,
            t.source_table,
            connection_poll.type,
            t.last_write,
            t.upload_record,
            t.redis_message_id,
            t_arm_list,
        )
    ]
    return t_list


def get_upload_record(poll_pk) -> int:
    from src.apps.core.models import ConnectSet, ImportTables

    connection_poll = ConnectSet.consets.record(pk=poll_pk)
    t_list = [
        RecordInfo(
            t.connects.source_conection.slug_name,
            t.source_table,
            t.connects.dest_conection.slug_name,
            t.dest_table,
            t.dest_table,
            t.connects.type,  # import type: DBF / ARM
            t.last_write,
            ARMCount(
                source_connection_name=t.connects.source_conection.slug_name,
                source_table_name=t.source_table,
                dest_connection_name=t.connects.dest_conection.slug_name,
                dest_table_name=t.dest_table,
            ).count(),
        )
        for t in ImportTables.tables.tables_for_import(connection_poll.pk) \
        ]
    return t_list


def table_import_info(table_pk) -> ImportInfo:
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
        )
    ]
    return t_list


def update_message_id(message_data: dict) -> None:
    from src.apps.core.models import ImportTables
    kwargs = message_data['kwargs']
    message_id = message_data['message_id']
    table_pk = kwargs['table_pk']
    record_to_update = ImportTables.tables.filter(pk=table_pk)
    record_to_update.update(message_id=message_id)


def update_last_import_date(message_data, result):
    """Update the date and time of last write uploaded data from the import table"""
    from src.apps.core.models import ImportTables

    databases = settings.DATABASES
    kwargs = message_data['kwargs']
    table_pk = kwargs['table_pk']
    message_id = message_data['message_id']
    type = kwargs['type']
    source_connection_name = kwargs['source_connection_name']
    source_databases = databases[kwargs['source_connection_name']]

    print("################################################################################")
    print(f"############ Message id {message_id} is success ########")
    print("################################################################################")

    record_to_update = ImportTables.tables.filter(pk=table_pk)

    if source_databases:
        data_directory = source_databases["NAME"]
        source_table = f"{kwargs['source_table_name']}"
        if type == ETL.EXPORT.DBF:
            # Get last write file date
            last_write = get_last_dbf_file_modify_date(data_directory, source_table)
            print("################################################################################")
            print(f"#### Success import from file {data_directory}{source_table}.DBF : "
                  f"last write was at {last_write}  ####")
            print("################################################################################")
        else:
            last_write = datetime.today()
            print("################################################################################")
            print(f"#### Success import from database {source_connection_name} table {source_table} : "
                  f"last write was at {last_write}  ####")
            print("################################################################################")

        if last_write:
            # last_write = datetime.fromtimestamp(last_write_time, tz=pytz.timezone(settings.TIME_ZONE)).strftime('%Y-%m-%d %H:%M:%S')
            record_to_update.update(last_write=last_write)

        if result:
            print("#########################################################")
            print(f"############# {result} records has been imported #######")
            print("#########################################################")
            record_to_update.update(upload_record=result)
        # Update import_table redis message id
        # update_message_id(message_data)
