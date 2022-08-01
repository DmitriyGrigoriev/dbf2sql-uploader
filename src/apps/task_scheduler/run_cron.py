import logging
import signal
# from src.apps.task_scheduler.tasks import print_current_datetime

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['E:\\MyDocuments\\Projects\\code\\dbf2sql-uploader', 'D:\\MyPrograms\\JetBrains\\PyCharm 2020.1\\plugins\\python\\helpers\\pycharm', 'D:\\MyPrograms\\JetBrains\\PyCharm 2020.1\\plugins\\python\\helpers\\pydev'])

from src.apps.task_scheduler import cron
from src.apps.task_scheduler.tasks import print_current_datetime
from apscheduler.schedulers.blocking import BlockingScheduler

logging.basicConfig(
    format="[%(asctime)s] [PID %(process)d] [%(threadName)s] [%(name)s] [%(levelname)s] %(message)s",
    level=logging.DEBUG,
)

# Pika is a bit noisy w/ Debug logging so we have to up its level.
logging.getLogger("pika").setLevel(logging.WARNING)


def main():
    scheduler = BlockingScheduler()
    for trigger, module_path, func_name in cron.JOBS:
        job_path = f"{module_path}:{func_name}.send"
        job_name = f"{module_path}.{func_name}"
        scheduler.add_job(job_path, trigger=trigger, name=job_name)

    def shutdown(signum, frame):
        scheduler.shutdown()

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    scheduler.start()
    return 0


if __name__ == "__main__":
    # import django;
    #
    # print('Django %s' % django.get_version())
    # if 'setup' in dir(django): django.setup()
    # import django_manage_shell;

    # django_manage_shell.run(PROJECT_ROOT)
    sys.exit(main())