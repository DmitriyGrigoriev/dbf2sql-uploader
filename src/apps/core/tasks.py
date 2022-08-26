# import time
import redis
import dramatiq
from dramatiq.rate_limits import ConcurrentRateLimiter
from dramatiq.rate_limits.backends import RedisBackend

import dataclasses
from src.config import settings
from src.apps.common.dataclasses import ImportInfo
# from django_dramatiq.models import Task
from src.services.sqlimport import SQLImport
from src.apps.core.models import ImportTables


@dramatiq.actor
def hello():
    hello.logger.info("Hello from hello() func")
    print(f"Hello there import")


@dramatiq.actor
def identity(x):
    return x


def process_database_import(params: ImportInfo):
    # dataclass:ImportInfo
    # ----------------------------
    # table_pk: int,
    # object_pk: int,
    # source_connection_name: str,
    # source_table_name: str,
    # dest_connection_name: str,
    # dest_table_name: str,
    # type: str
    # -----------------------------
    for p in params:
        # kwargs = ImportTables.tables.get_kwargs(table_pk=p.table_pk)
        process_import.send_with_options(
            kwargs=dataclasses.asdict(p),
            # args=(object_pk, source_connection_name, source_table, dest_connection_name, dest_table),
            on_failure=print_error,
            on_success=update_last_write_if_success_result,
        )


@dramatiq.actor(max_retries=0, time_limit=settings.ONE_HOUR*3)
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
    # type: str
    global result
    result = 0
    try:
        backend = RedisBackend(url=settings.DRAMATIQ_REDIS_URL)
        DISTRIBUTED_MUTEX = ConcurrentRateLimiter(backend, f"distributed-mutex-{kwargs['table_pk']}", limit=1)
        # {'table_pk': 132, 'poll_pk': 1, 'source_connection_name': 'dbf_borodki_2022', 'source_table_name': 'PZK_RSN',
        #  'dest_connection_name': 'dbf_borodki_2022', 'dest_table_name': 'TPZK_RSN'}
        with DISTRIBUTED_MUTEX.acquire():
            print('########### DISTRIBUTED_MUTEX.acquire ###########')
            # print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            # print(f'{settings.DATABASES}')
            # print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
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
    exception_type = exception_data['type']
    if exception_type == 'RateLimitExceeded':
        redis_message_id = message_data['options']['redis_message_id']
        redis_client = redis.Redis(host=f"{settings.REDIS_HOST}", port=f"{settings.REDIS_PORT}", db=0)
        redis_client.hdel("dramatiq:default.DQ.msgs", redis_message_id)
        print(f"############ Redis message_id {redis_message_id} was deleted due to {exception_type} #########")
        print("################################################################################")

    # print_error.logger.info("################################################################################")
    # print_error.logger.info(f"  * exception_data: {exception_data}")
    # print_error.logger.info("################################################################################")
    # print_error.logger.info(f"  * message_data: {message_data}!r")
    # print_error.logger.info("################################################################################")

    # {'queue_name': 'default', 'actor_name': 'process_import', 'args': [],
    #  'kwargs': {'table_pk': 270, 'poll_pk': 4, 'source_connection_name': 'dbf_2022_test',
    #             'source_table_name': 'DCLHEAD', 'dest_connection_name': 'local_2022_test',
    #             'dest_table_name': 'TDCLHEAD'},
    #  'options': {'on_failure': 'print_error', 'on_success': 'update_last_write_if_success_result',
    #              'redis_message_id': 'e9ce6195-9303-4061-8da7-54fe7a66ad32', 'retries': 1,
    #              'traceback': 'Traceback (most recent call last):\n  File "E:\\MyDocuments\\Projects\\code\\dbf2sql-uploader\\.venv\\lib\\site-packages\\dramatiq\\worker.py", line 485, in process_message\n    res = actor(*message.args, **message.kwargs)\n  File "E:\\MyDocuments\\Projects\\code\\dbf2sql-uploader\\.venv\\lib\\site-packages\\dramatiq\\actor.py", line 145, in __call__\n    return self.fn(*args, **kwargs)\n  File ".\\src\\apps\\core\\tasks.py", line 54, in process_import\n    with DISTRIBUTED_MUTEX.acquire():\n  File "E:\\MyDocuments\\Projects\\code\\dbf2sql-uploader\\.venv\\lib\\site-packages\\colorama\\ansitowin32.py", line 41, in write\n    self.__convertor.write(text)\n  File "E:\\MyDocuments\\Projects\\code\\dbf2sql-uploader\\.venv\\lib\\site-packages\\colorama\\ansitowin32.py", line 162, in write\n    self.write_and_convert(text)\n  File "E:\\MyDocuments\\Projects\\code\\dbf2sql-uploader\\.venv\\lib\\site-packages\\colorama\\ansitowin32.py", line 190, in write_and_convert\n    self.write_plain_text(text, cursor, len(text))\n  File "E:\\MyDocuments\\Projects\\code\\dbf2sql-uploader\\.venv\\lib\\site-packages\\colorama\\ansitowin32.py", line 195, in write_plain_text\n    self.wrapped.write(text[start:end])\n  File "E:\\MyDocuments\\Projects\\code\\dbf2sql-uploader\\.venv\\lib\\site-packages\\dramatiq\\compat.py", line 55, in write\n    self.pipe.send_bytes(s.encode(self.encoding, errors="replace"))\n  File "D:\\MyPrograms\\Python\\Python38\\lib\\multiprocessing\\connection.py", line 200, in send_bytes\n    self._send_bytes(m[offset:offset + size])\n  File "D:\\MyPrograms\\Python\\Python38\\lib\\multiprocessing\\connection.py", line 280, in _send_bytes\n    ov, err = _winapi.WriteFile(self._handle, buf, overlapped=True)\nBrokenPipeError: [WinError 232] Идет закрытие канала\n'},
    #  'message_id': '71568637-eca5-4171-ae05-d1b0ffc50f9a', 'message_timestamp': 1660994562798}

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

# dramatiq --path . --processes 4 --threads 4 src.config.setup django_dramatiq.tasks src.apps.core.tasks src.apps.task_scheduler.tasks
