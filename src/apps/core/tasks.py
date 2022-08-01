import time
import dramatiq
from dramatiq.rate_limits import ConcurrentRateLimiter
from dramatiq.rate_limits.backends import RedisBackend

from src.config import settings
from src.services.dataclasses import ImportInfo
# from django_dramatiq.models import Task
from src.services.sqlimport import SQLImport
from src.apps.core.models import ImportTables, ConnectSet


@dramatiq.actor
def hello():
    hello.logger.info("Hello from hello() func")
    print(f"Hello there import")


@dramatiq.actor
def identity(x):
    return x


def process_database_import(params: ImportInfo):
    for p in params:
        kwargs = ImportTables.tables.get_kwargs(table_pk=p.table_pk)
        process_import.send_with_options(
            kwargs=kwargs,
            # args=(object_pk, source_connection_name, source_table, dest_connection_name, dest_table),
            on_failure=print_error,
            on_success=update_last_write_if_success_result,
        )


@dramatiq.actor(max_retries=0, time_limit=settings.ONE_HOUR)
def process_import(
        *args,
        **kwargs
) -> int:
    # table_pk: int,
    # object_pk: int,
    # source_connection_name: str,
    # source_table_name: str,
    # dest_connection_name: str,
    # dest_table_name: str,
    global result
    result = 0
    try:
        backend = RedisBackend(url=settings.DRAMATIQ_REDIS_URL)
        DISTRIBUTED_MUTEX = ConcurrentRateLimiter(backend, f"distributed-mutex-{kwargs['table_pk']}", limit=1)
        # {'table_pk': 132, 'poll_pk': 1, 'source_connection_name': 'dbf_borodki_2022', 'source_table_name': 'PZK_RSN',
        #  'dest_connection_name': 'dbf_borodki_2022', 'dest_table_name': 'TPZK_RSN'}
        with DISTRIBUTED_MUTEX.acquire():
            print('########### DISTRIBUTED_MUTEX.acquire ###########')
            # print(f'%%%%% {kwargs} %%%%%%')
            print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            print(f'{settings.DATABASES}')
            print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            result = SQLImport(
                source_connection_name=kwargs.pop('source_connection_name'),
                source_table_name=kwargs.pop('source_table_name'),
                dest_connection_name=kwargs.pop('dest_connection_name'),
                dest_table_name=kwargs.pop('dest_table_name'),
                logger=process_import.logger
            ).start_import()
    except dramatiq.RateLimitExceeded:
        # process_import.logger.info('############ dramatiq.RateLimitExceeded ###########')
        raise dramatiq.RateLimitExceeded('############ dramatiq.RateLimitExceeded ###########')

    # print(f"############ Has been imported {result} records ########")

    return result

@dramatiq.actor
def update_last_write_if_success_result(message_data, result):
    """Update last_write field by current datetime from DBF file"""
    ImportTables.tables.update_last_import_date(message_data, result)


@dramatiq.actor
def print_error(message_data, exception_data):
    print("################################################################################")
    print(f"############ Message id {message_data['message_id']} is failed #########")
    print("################################################################################")
    # print(f"  * type: {exception_data['type']}")
    # print(f"  * message: {exception_data['message']!r}")
    # print_error.logger.info(f"Message {message_data['message_id']} failed:")
    # print_error.logger.info(f"  * type: {exception_data['type']}")
    # print_error.logger.info(f"  * message: {exception_data['message']!r}")

    # process_import.logger.info(message.get_result(block=True, timeout=60))


# from django_dramatiq.setup import
# python manage.py rundramatiq --worker-shutdown-timeout 3600000
# dramatiq --path . --processes 4 --threads 4 --worker-shutdown-timeout 3600000 django_dramatiq.setup django_dramatiq.tasks src.apps.core.tasks
# dramatiq --path . --log-file ./logs/dramatiq.log --processes 4 --threads 4 django_dramatiq.setup django_dramatiq.tasks src.apps.core.tasks
# dramatiq --path . --processes 4 --threads 4 django_dramatiq.setup django_dramatiq.tasks src.apps.core.tasks
# dramatiq --path . --processes 4 --threads 4  --pid-file ./logs/pid.log django_dramatiq.setup django_dramatiq.tasks src.apps.core.tasks src.apps.task_scheduler.tasks

# dramatiq --path . --processes 4 --threads 4  --pid-file ./logs/pid.log src.config.setup django_dramatiq.tasks src.apps.core.tasks src.apps.task_scheduler.tasks
