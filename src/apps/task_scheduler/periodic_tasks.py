import os
from datetime import datetime
import logging

from .tasks import process_user_stats


def periodically_run_job():
    """This task will be run by APScheduler.
    It can prepare some data and parameters and then enqueue background task.
    """
    last_write_time = os.path.getmtime('\\\\192.168.89.213\\FTSBASES\\GTD_2022_BOROD\\Pzk_Rsn.DBF')
    last_write = datetime.fromtimestamp(last_write_time).strftime('%Y-%m-%d %H:%M:%S')
    logging.warning(f'LAST WRITE TIME:{last_write}')
    # logging.warning('It is time to start the dramatiq task')
    # process_user_stats.send()


# python manage.py run_scheduler