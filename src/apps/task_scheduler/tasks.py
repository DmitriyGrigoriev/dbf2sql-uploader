import logging
# import time
import dramatiq
from src.apps.task_scheduler.cron import cron
from src.apps.core.models import ConnectSet, ImportTables
from src.apps.core.tasks import process_database_import
from src.apps.common.dataclasses import ImportInfo

# logging.basicConfig(
#     format="[%(asctime)s] [PID %(process)d] [%(threadName)s] [%(name)s] [%(levelname)s] %(message)s",
#     level=logging.DEBUG,
# )

# Pika is a bit noisy w/ Debug logging so we have to up its level.
logger = logging.getLogger(__name__)

# @cron("* * * * *")  # Run once a minute
# @dramatiq.actor()
# def print_current_datetime():
#     logging.warning('Start my long-running task')
#     time.sleep(5)
#     logging.warning(f'Last write time is: {datetime.now()}')


# @cron("* * * * *")  # Run once a minute
# @dramatiq.actor()
# def process_user_stats():
#     """Very simple task for demonstrating purpose."""
#     logging.warning('Start my long-running task')
#     time.sleep(5)
#     logging.warning('Task is ended')

@cron("*/20 * * * *")  # Run once 20 minutes
@dramatiq.actor()
def select_tables_for_imports():
    """Just do reimport it data from DBF tables if they have  changed last write date time"""
    # https://linuxize.com/post/cron-jobs-every-5-10-15-minutes/

    data_polls = ConnectSet.consets.allowed_for_import()
    for data in data_polls:
        params: ImportInfo = ImportTables.tables.table_import_info(data.pk)
        # params = ImportTables.tables.tables_import_list(data.pk)
        if len(params) > 0:
            print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            logging.info(f'%%%%%%% Selected tables for import {params} %%%%%%%%')
            print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            process_database_import(params=params)
        else:
            print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            logging.info(f'%%%%%%% No selected tables for import data %%%%%%%%')
            print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

# python manage.py run_scheduler