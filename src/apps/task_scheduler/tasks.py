import logging
import dramatiq
from src.apps.task_scheduler.cron import cron
from django_dramatiq.tasks import delete_old_tasks
from src.apps.core.tasks import process_database_import
from src.apps.core.functions import tables_import_info_list

# logging.basicConfig(
#     format="[%(asctime)s] [PID %(process)d] [%(threadName)s] [%(name)s] [%(levelname)s] %(message)s",
#     level=logging.DEBUG,
# )

logger = logging.getLogger(__name__)

@cron("*/20 * * * *")  # Run once 20 minutes
@dramatiq.actor()
def select_tables_for_imports():
    """Just do reimport it data from DBF tables if they have  changed last write date time"""
    # https://linuxize.com/post/cron-jobs-every-5-10-15-minutes/
    from src.apps.core.models import ConnectSet

    data_polls = ConnectSet.consets.allowed_for_import()
    for poll in data_polls:
        params = tables_import_info_list(poll.pk)
        if len(params) > 0:
            logging.info(f'%%%%%%% Selected tables for import {params} %%%%%%%%')
            process_database_import(params=params)
        else:
            logging.info(f'%%%%%%% No selected tables for import %%%%%%%%')


# @cron("* * * 3 *")  # Run once 20 minutes
@cron("*/20 * * * *")
@dramatiq.actor()
def delete_journal_tasks():
    delete_old_tasks(max_task_age=864000)

# python manage.py run_scheduler