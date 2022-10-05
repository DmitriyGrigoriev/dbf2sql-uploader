import time
import dataclasses
from typing import Any
from typing import Dict
from typing import List

import dramatiq
from dramatiq.rate_limits import ConcurrentRateLimiter
from dramatiq.rate_limits.backends import RedisBackend

from src.apps.common.dataclasses import ETL
from src.apps.common.dataclasses import ImportInfo
from src.apps.common.functions import get_redis_client
from src.apps.core.functions import update_last_import_date
from src.apps.core.functions import update_message_id
from src.config import settings
from src.services.armimport import ARMImport
from src.services.sqlimport import SQLImport

assert isinstance(ETL.MODE, object)

@dramatiq.actor(store_results=True)
def wait(n):
    time.sleep(n)
    return str(n)


def test_groups_expose_completion_stats():
    # When I group multiple of these actors together and run them
    # t = time.monotonic()
    # g = group([wait.message() for _ in range(5)])
    # g.run()

    # And wait on the group to complete
    # results = list(g.get_results(block=True))

    group = dramatiq.group([wait.send(x) for x in range(5)]).run()

    from dramatiq.results import ResultTimeout
    try:
        results = group.get_results(block=True, timeout=100)
        # results = itertools.chain(*[x for x in group.get_results(block=True, timeout=100)])
    except ResultTimeout:
        print('########## ResultTimeout ##########')
        raise ResultTimeout('########## ResultTimeout ##########')

    # print(set(results))


    # # Then the total elapsed time should be less than 500ms
    # assert time.monotonic() - t <= 0.5
    #
    # # And I should get back as many results as there were jobs in the group
    # assert len(results) == len(g)
    #
    # # And the group should be completed
    # assert g.completed


def process_database_import(
    params: List[ImportInfo], mode: str = ETL.MODE.FULL
) -> None:
    """

    :param params: ImportInfo{
        table_pk: int,
        object_pk: int,
        source_connection_name: str,
        source_table_name: str,
        dest_connection_name: str,
        dest_table_name: str,
        type: str
    }
    :type mode: str
    """
    for p in params:
        kwargs = dataclasses.asdict(p)
        kwargs.update({"mode": mode})

        process_import.send_with_options(
            kwargs=kwargs,
            # args=(object_pk, source_connection_name, source_table, dest_connection_name, dest_table),
            on_failure=print_error,
            on_success=update_last_write_if_success_result,
        )


@dramatiq.actor(
    store_results=True, max_retries=0, time_limit=ETL.TIMELMIT.SIX_HOUR
)
def process_import(*, args=None, **kwargs) -> int:
    """

    :param args:
    :param kwargs: {
        table_pk: int,
        object_pk: int,
        source_connection_name: str,
        source_table_name: str,
        dest_connection_name: str,
        dest_table_name: str,
        type: str,
    }
    :return:
    """
    table_pk = kwargs["table_pk"]
    type = kwargs["type"]
    mode = kwargs["mode"]
    try:
        backend = RedisBackend(url=settings.DRAMATIQ_REDIS_URL)
        DISTRIBUTED_MUTEX = ConcurrentRateLimiter(
            backend, f"distributed-mutex-{table_pk}", limit=1
        )
        with DISTRIBUTED_MUTEX.acquire():
            print("########### DISTRIBUTED_MUTEX.acquire ###########")
            if type == ETL.EXPORT.DBF:
                data_directory = kwargs.pop("source_connection_name")
                source_table = kwargs.pop("source_table_name")
                return SQLImport(
                    source_connection_name=data_directory,
                    source_table_name=source_table,
                    dest_connection_name=kwargs.pop("dest_connection_name"),
                    dest_table_name=kwargs.pop("dest_table_name"),
                    logger=process_import.logger,
                    mode=mode,
                ).start_import()
            else:
                # type == 'ARM'
                source_connection = kwargs.pop("source_connection_name")
                source_table = kwargs.pop("source_table_name")
                dest_connection = kwargs.pop("dest_connection_name")
                dest_table = kwargs.pop("dest_table_name")
                return ARMImport(
                    source_connection_name=source_connection,
                    source_table_name=source_table,
                    dest_connection_name=dest_connection,
                    dest_table_name=dest_table,
                    logger=process_import.logger,
                    mode=mode,
                ).start_import()
    except dramatiq.RateLimitExceeded:
        raise dramatiq.RateLimitExceeded(
            "############ dramatiq.RateLimitExceeded ###########"
        )



@dramatiq.actor(
    store_results=True, max_retries=0, time_limit=ETL.TIMELMIT.SIX_HOUR
)
def process_import(*, args=None, **kwargs) -> int:
    """

    :param args:
    :param kwargs: {
        table_pk: int,
        object_pk: int,
        source_connection_name: str,
        source_table_name: str,
        dest_connection_name: str,
        dest_table_name: str,
        type: str,
    }
    :return:
    """
    table_pk = kwargs["table_pk"]
    type = kwargs["type"]
    mode = kwargs["mode"]
    try:
        backend = RedisBackend(url=settings.DRAMATIQ_REDIS_URL)
        DISTRIBUTED_MUTEX = ConcurrentRateLimiter(
            backend, f"distributed-mutex-{table_pk}", limit=1
        )
        with DISTRIBUTED_MUTEX.acquire():
            print("########### DISTRIBUTED_MUTEX.acquire ###########")
            if type == ETL.EXPORT.DBF:
                data_directory = kwargs.pop("source_connection_name")
                source_table = kwargs.pop("source_table_name")
                return SQLImport(
                    source_connection_name=data_directory,
                    source_table_name=source_table,
                    dest_connection_name=kwargs.pop("dest_connection_name"),
                    dest_table_name=kwargs.pop("dest_table_name"),
                    logger=process_import.logger,
                    mode=mode,
                ).start_import()
            else:
                # type == 'ARM'
                source_connection = kwargs.pop("source_connection_name")
                source_table = kwargs.pop("source_table_name")
                dest_connection = kwargs.pop("dest_connection_name")
                dest_table = kwargs.pop("dest_table_name")
                return ARMImport(
                    source_connection_name=source_connection,
                    source_table_name=source_table,
                    dest_connection_name=dest_connection,
                    dest_table_name=dest_table,
                    logger=process_import.logger,
                    mode=mode,
                ).start_import()
    except dramatiq.RateLimitExceeded:
        raise dramatiq.RateLimitExceeded(
            "############ dramatiq.RateLimitExceeded ###########"
        )


@dramatiq.actor
def update_last_write_if_success_result(
    message_data: Dict[Any, Any], result: int
) -> None:
    """Update last_write field by current datetime from DBF file"""
    update_last_import_date(message_data, result)


@dramatiq.actor
def print_error(
    message_data: Dict[Any, Any], exception_data: Dict[Any, Any]
) -> None:
    print(
        f"############ Task message_id {message_data['message_id']} was failed #########"
    )
    exception_type = exception_data["type"]
    if exception_type == "RateLimitExceeded":
        redis_message_id = message_data["options"]["redis_message_id"]
        redis_client = get_redis_client()
        redis_client.hdel(ETL.DRAMATIQ.DRAMATIQ_MSGS, redis_message_id)

        print(
            f"############ Task Redis message_id {redis_message_id} was deleted by {exception_type} #########"
        )
    else:
        update_message_id(message_data)

    # print_error.logger.info("################################################################################")
    # print_error.logger.info(f"  * exception_data: {exception_data}")
    # print_error.logger.info("################################################################################")
    # print_error.logger.info(f"  * message_data: {message_data}!r")
    # print(f"  * type: {exception_data['type']}")
    # print(f"  * message: {exception_data['message']!r}")
    # print_error.logger.info(f"Message {message_data['message_id']} failed:")
    # print_error.logger.info(f"  * type: {exception_data['type']}")
    # print_error.logger.info(f"  * message: {exception_data['message']!r}")

    # process_import.logger.info(message.get_result(block=True, timeout=60))

    # python manage.py rundramatiq --worker-shutdown-timeout 3600000
    # dramatiq --path . --processes 4 --threads 4  --pid-file ./logs/pid.log django_dramatiq.setup django_dramatiq.tasks src.apps.core.tasks src.apps.task_scheduler.tasks


# dramatiq --path . --processes 4 --threads 4 src.config.setup django_dramatiq.tasks src.apps.core.tasks src.apps.task_scheduler.tasks
