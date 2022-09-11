from datetime import datetime
from src.config import settings
from src.apps.common.dataclasses import ETL
from src.apps.common.functions import get_last_dbf_file_modify_date
from src.apps.core.models import ImportTables

def update_message_id(message_data: dict) -> None:
    kwargs = message_data['kwargs']
    table_pk = kwargs['table_pk']
    message_id = message_data['message_id']
    record_to_update = ImportTables.tables.filter(pk=table_pk)
    record_to_update.update(message_id=message_id)


def update_last_import_date(message_data, result):
    """Update the date and time of last write uploaded data from the import table"""
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
            print(
                f"#### Success import from file {data_directory}{source_table}.DBF : last write was at {last_write}  ####")
            print("################################################################################")
        else:
            last_write = datetime.today()
            print("################################################################################")
            print(
                f"#### Success import from database {source_connection_name} table {source_table} : last write was at {last_write}  ####")
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
        update_message_id(message_data)
