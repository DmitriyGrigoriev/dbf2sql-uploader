import logging
import signal
from django.core.management.base import BaseCommand, CommandError
from apscheduler.schedulers.background import BlockingScheduler

# from apscheduler.triggers.cron import CronTrigger
# from src.apps.task_scheduler.periodic_tasks import periodically_run_job

from src.apps.task_scheduler import cron
# from src.apps.task_scheduler.tasks import print_current_datetime
# from src.apps.task_scheduler.tasks import select_tables_for_imports


logging.basicConfig(
    format="[%(asctime)s] [PID %(process)d] [%(threadName)s] [%(name)s] [%(levelname)s] %(message)s",
    level=logging.DEBUG,
)

class Command(BaseCommand):
    help = 'Run blocking scheduler to create periodical tasks'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Preparing scheduler'))
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

        # python manage.py run_scheduler

        # scheduler = BlockingScheduler(timezone=pytz.timezone(settings.TIME_ZONE))
        # every_day_at_8_30 = CronTrigger(day_of_week='mon-fri', hour='8', minute='30,45', timezone=settings.TIME_ZONE)
        # every_day_every_10 = CronTrigger(day_of_week='mon-fri', hour='9-15', minute='*/1', timezone=settings.TIME_ZONE)
        # every_day_at_05_05_utc = CronTrigger(minute=1, timezone=pytz.UTC)
        # trigger = OrTrigger([every_day_at_8_30, every_day_every_10])
        # scheduler.add_job(periodically_run_job, trigger)
        # scheduler.add_job(periodically_run_job, trigger='interval', seconds=60)
        # ... add another jobs
        # self.stdout.write(self.style.NOTICE('Start scheduler'))
        # scheduler.start()

        # def shutdown(signum, frame):
        #     scheduler.shutdown()
        #
        # try:
        #     scheduler.start()
        # except (KeyboardInterrupt):
        #     scheduler.shutdown()
        #     signal.signal(signal.SIGINT, shutdown)
        #     signal.signal(signal.SIGTERM, shutdown)
        #     logger.debug('Got SIGTERM! Terminating...')
