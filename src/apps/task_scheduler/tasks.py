import logging
# import time
import dramatiq
from src.apps.task_scheduler.cron import cron
from src.apps.core.managers import ConnectSetManager
from src.apps.core.tasks import process_database_import
from src.apps.core.functions import tables_import_info_list

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

    data_polls = ConnectSetManager.allowed_for_import()
    for poll in data_polls:
        params = tables_import_info_list(poll.pk)
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