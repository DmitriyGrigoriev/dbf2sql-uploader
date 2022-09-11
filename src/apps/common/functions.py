import os
from datetime import datetime, timezone

def get_last_dbf_file_modify_date(data_directory, file_name) -> datetime:
    """
    Return the last time modifying DBF file

    :param data_directory:
    :param file_name:
    :return:
    """
    file_name = f"{data_directory}{file_name}.DBF"
    last_write = None
    if os.path.isfile(file_name):
        last_write = datetime.fromtimestamp(os.path.getmtime(file_name), tz=timezone.utc)

    return last_write
