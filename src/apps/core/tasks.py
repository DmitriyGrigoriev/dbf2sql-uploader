import json
import logging
from typing import Any
from typing import Dict
from typing import List

import dramatiq
from dramatiq.rate_limits import ConcurrentRateLimiter
from dramatiq.rate_limits.backends import RedisBackend

from django.template import loader
from django.core.mail import mail_admins
from src.apps.common.dataclasses import ETL
from src.apps.common.dataclasses import ImportInfo
from src.apps.common.functions import get_redis_client
from src.apps.core.functions import update_last_import_date
from src.apps.core.functions import update_message_id
from src.config import settings
from src.services.armimport import ARMImport
from src.services.sqlimport import SQLImport
# from src.services.pipelines import PipeLineController
# from src.services.pipe_sqlimport import PipeSQLImport, PipeSQLLocalFts

assert isinstance(ETL.MODE, object)

logger = logging.getLogger(__name__)

def process_database_import(params: List[ImportInfo]) -> None:
    """
    :param params: ImportInfo
    """
    p: ImportInfo
    for p in params:
        kwargs = p.to_dict() #{"params": p.to_json()}
        process_import.send_with_options(
            kwargs=kwargs,
            # args=(object_pk, source_connection_name, source_table, dest_connection_name, dest_table),
            on_failure=print_error,
            on_success=update_last_write_if_success_result,
        )


@dramatiq.actor(
    store_results=True, max_retries=0, time_limit=ETL.TIMELMIT.SIX_HOUR
)
def process_import(*, args=None, **kwargs: dict) -> int:
    """

    :param args:
    :param kwargs: ImportInfo
    :return: int
    """
    params = ImportInfo.from_dict(kwargs)
    try:
        backend = RedisBackend(url=settings.DRAMATIQ_REDIS_URL)
        PROCESS_MUTEX = ConcurrentRateLimiter(
            backend, f"mutex-{params.source_table_name.lower()}-{params.table_pk}", limit=1
        )
        with PROCESS_MUTEX.acquire():
            print(f"########### PROCESS_MUTEX: mutex-{params.source_table_name.lower()}-"
                  f"{params.table_pk}' ###########")
            if params.type == ETL.EXPORT.DBF:
                return SQLImport(params).run_import()

            if params.type == ETL.EXPORT.DOC2SQL:
                return ARMImport(params).run_import()
    except dramatiq.RateLimitExceeded:
        raise dramatiq.RateLimitExceeded(
            f"############ RateLimitExceeded: {params.source_table_name} ###########"
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
        if not settings.DEBUG:
            # >> > from django.template import Context, Template
            # >> > template = Template("Hello {{ name }}!")
            # >> > context = Context({'name': "world"})
            # >> > template.render(context)
            # 'Hello world!'
            traceback: dict = message_data['options'].pop('traceback')
            ctx = {
                'message_id': message_data['message_id'],
                'message_data': json.dumps(message_data, indent=4),
                'traceback': traceback.split('\n')
            }
            mail_admins(
                subject=f" message {message_data['message_id']} failed",
                message=f"############ Message {message_data['message_id']} failed #########",
                html_message=loader.get_template("tasks/core/dramatiq_exception.html").render(ctx),
            )

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
    # dramatiq --path . --processes 4 --threads 4  --pid-file
    # ./logs/pid.log django_dramatiq.setup django_dramatiq.tasks
    # src.apps.core.tasks src.apps.task_scheduler.tasks


# dramatiq --path . --processes 4 --threads 4 src.config.setup
# django_dramatiq.tasks src.apps.core.tasks src.apps.task_scheduler.tasks


# def test_process_database_import(params: List[ImportInfo]) -> None:
#     p: ImportInfo
#     for p in params:
#         kwargs = dataclasses.asdict(p)
#
#         test_process_import.send_with_options(
#             kwargs=kwargs,
#             on_failure=print_error,
#             on_success=update_last_write_if_success_result,
#         )


# @dramatiq.actor(
#     store_results=True, max_retries=0, time_limit=ETL.TIMELMIT.SIX_HOUR
# )
# def test_process_import(*, args=None, **kwargs) -> int:
#     table_pk = kwargs["table_pk"]
#     type = kwargs["type"]
#     mode = kwargs["mode"]
#     try:
#         backend = RedisBackend(url=settings.DRAMATIQ_REDIS_URL)
#         DISTRIBUTED_MUTEX = ConcurrentRateLimiter(
#             backend, f"distributed-mutex-{table_pk}", limit=1
#         )
#         with DISTRIBUTED_MUTEX.acquire():
#             print(f"########### DISTRIBUTED_MUTEX({kwargs['source_table_name']}) ###########")
#             if type == ETL.EXPORT.DBF:
#                 data_directory = kwargs["source_connection_name"]
#                 source_table = kwargs["source_table_name"]
#                 print(f"Process: {kwargs['source_table_name']}")
#                 time.sleep(600)
#                 # return SQLImport(
#                 #     source_connection_name=data_directory,
#                 #     source_table_name=source_table,
#                 #     dest_connection_name=kwargs.pop("dest_connection_name"),
#                 #     dest_table_name=kwargs.pop("dest_table_name"),
#                 #     # logger=process_import.logger,
#                 #     mode=mode,
#                 # ).start_import()
#             else:
#                 # type == 'ARM'
#                 source_connection = kwargs["source_connection_name"]
#                 source_table = kwargs["source_table_name"]
#                 dest_connection = kwargs["dest_connection_name"]
#                 dest_table = kwargs["dest_table_name"]
#                 for x in range(1, 100):
#                     print(f"Process: {kwargs['source_table_name']}")
#                     time.sleep(6)
#                 # return ARMImport(
#                 #     source_connection_name=source_connection,
#                 #     source_table_name=source_table,
#                 #     dest_connection_name=dest_connection,
#                 #     dest_table_name=dest_table,
#                 #     # logger=process_import.logger,
#                 #     mode=mode,
#                 # ).start_import()
#     except dramatiq.RateLimitExceeded:
#         raise dramatiq.RateLimitExceeded(
#             f"############ RateLimitExceeded({kwargs['source_table_name']}) ###########"
#         )
# @dramatiq.actor(store_results=True)
# def wait(n):
#     time.sleep(n)
#     return str(n)
# def test_groups_expose_completion_stats():
#     # When I group multiple of these actors together and run them
#     # t = time.monotonic()
#     # g = group([wait.message() for _ in range(5)])
#     # g.run()
#
#     # And wait on the group to complete
#     # results = list(g.get_results(block=True))
#
#     group = dramatiq.group([wait.send(x) for x in range(5)]).run()
#
#     from dramatiq.results import ResultTimeout
#     try:
#         results = group.get_results(block=True, timeout=100)
#         # results = itertools.chain(*[x for x in group.get_results(block=True, timeout=100)])
#     except ResultTimeout:
#         print('########## ResultTimeout ##########')
#         raise ResultTimeout('########## ResultTimeout ##########')
#
#     # print(set(results))
#
#
#     # # Then the total elapsed time should be less than 500ms
#     # assert time.monotonic() - t <= 0.5
#     #
#     # # And I should get back as many results as there were jobs in the group
#     # assert len(results) == len(g)
#     #
#     # # And the group should be completed
#     # assert g.completed
# def delete_redis_message(redis_message_id):
#     redis_client = get_redis_client()
#     redis_client.hdel(ETL.DRAMATIQ.DRAMATIQ_MSGS, redis_message_id)
#     logger.info(
#         f"############ Task Redis message_id {redis_message_id} was deleted by RateLimitExceeded #########"
#     )
#
#
# @dramatiq.actor(
#     store_results=True, max_retries=0, time_limit=ETL.TIMELMIT.SIX_HOUR
# )
# def delete_template_record(*args, **kwargs):
#     print("Message kwargs: ", kwargs)
#     return PipeSQLImport(
#         source_connection_name=kwargs['source_connection_name'],
#         source_table_name=kwargs['source_table_name'],
#         dest_connection_name=kwargs["dest_connection_name"],
#         dest_table_name=kwargs["dest_table_name"],
#     ).delete()
#     try:
#         process_pk = args
#         backend = RedisBackend(url=settings.DRAMATIQ_REDIS_URL)
#         DISTRIBUTED_MUTEX = ConcurrentRateLimiter(
#             backend, f"distributed-mutex-{process_pk}", limit=1
#         )
#         with DISTRIBUTED_MUTEX.acquire():
#             return PipeSQLImport(
#                 source_connection_name=kwargs['source_connection_name'],
#                 source_table_name=kwargs['source_table_name'],
#                 dest_connection_name=kwargs["dest_connection_name"],
#                 dest_table_name=kwargs["dest_table_name"],
#             ).delete()
#     except dramatiq.RateLimitExceeded:
#         # delete_redis_message(kwargs["options"]["redis_message_id"])
#         logger.error("############ RateLimitExceeded ###########")
# @dramatiq.actor(
#     store_results=True, max_retries=0, time_limit=ETL.TIMELMIT.SIX_HOUR
# )
# def export_from_dbf(*args, **kwargs):
#     return PipeSQLImport(
#         source_connection_name=kwargs['source_connection_name'],
#         source_table_name=kwargs['source_table_name'],
#         dest_connection_name=kwargs["dest_connection_name"],
#         dest_table_name=kwargs["dest_table_name"],
#     ).export()
#     try:
#         process_pk = args
#         backend = RedisBackend(url=settings.DRAMATIQ_REDIS_URL)
#         DISTRIBUTED_MUTEX = ConcurrentRateLimiter(
#             backend, f"distributed-mutex-{process_pk}", limit=1
#         )
#         with DISTRIBUTED_MUTEX.acquire():
#             return PipeSQLImport(
#                 source_connection_name=kwargs['source_connection_name'],
#                 source_table_name=kwargs['source_table_name'],
#                 dest_connection_name=kwargs["dest_connection_name"],
#                 dest_table_name=kwargs["dest_table_name"],
#             ).export()
#     except dramatiq.RateLimitExceeded:
#         logger.error("############ RateLimitExceeded ###########")
# @dramatiq.actor(
#     store_results=True, max_retries=0, time_limit=ETL.TIMELMIT.SIX_HOUR
# )
# def import_to_localfts(*args, **kwargs):
#     return PipeSQLLocalFts(
#         source_connection_name=kwargs['dest_connection_name'],
#         source_table_name=kwargs['dest_table_name'],
#         dest_connection_name=ETL.CONNECT.LOCALFTS,
#         dest_table_name=kwargs["dest_table_name"],
#     ).import_to_mssql()
#     try:
#         process_pk = args
#         backend = RedisBackend(url=settings.DRAMATIQ_REDIS_URL)
#         DISTRIBUTED_MUTEX = ConcurrentRateLimiter(
#             backend, f"distributed-mutex-{process_pk}", limit=1
#         )
#         with DISTRIBUTED_MUTEX.acquire():
#             return PipeSQLLocalFts(
#                 source_connection_name=kwargs['dest_connection_name'],
#                 source_table_name=kwargs['dest_table_name'],
#                 dest_connection_name=ETL.CONNECT.LOCALFTS,
#                 dest_table_name=kwargs["dest_table_name"],
#             ).import_to_mssql()
#     except dramatiq.RateLimitExceeded:
#         logger.error("############ RateLimitExceeded ###########")
# @dramatiq.actor(
#     store_results=True, max_retries=0, time_limit=ETL.TIMELMIT.SIX_HOUR
# )
# def pipeline_run(pk, pipes):
#     try:
#         backend = RedisBackend(url=settings.DRAMATIQ_REDIS_URL)
#         DISTRIBUTED_MUTEX = ConcurrentRateLimiter(
#             backend, f"distributed-mutex-{pk}", limit=1
#         )
#         with DISTRIBUTED_MUTEX.acquire():
#             pipeline(pipes).run()
#     except dramatiq.RateLimitExceeded:
#         logger.error("############ RateLimitExceeded ###########")
# def pipeline_steps_for_import(params: List[ImportInfo]):
#     return PipeLineController(params).do_runner()

    # for p in params:
    #     kwargs = dataclasses.asdict(p)
    #     kwargs.update({"mode": mode})
    #     etl_type = kwargs["type"]
    #     if etl_type == ETL.EXPORT.DBF:
    #         steps = [
    #             {
    #                 'name': 'delete',
    #                 'runner': delete_template_record,
    #                 'pipe_ignore': True
    #             },
    #             # {
    #             #     'name': 'export',
    #             #     'runner': export_from_dbf,
    #             #     'pipe_ignore': True
    #             # },
    #             # {
    #             #     'name': 'import',
    #             #     'runner': import_to_localfts,
    #             #     'pipe_ignore': False
    #             # }
    #         ]
    #
    #     pipes = []
    #     pk = kwargs["table_pk"]
    #     for step_num, step in enumerate(steps):
    #         # print(f"  Performing pipeline step {step['name']}")
    #         pipes.append(step['runner'].message_with_options(
    #             args=[pk],
    #             kwargs={'source_connection_name': kwargs["source_connection_name"],
    #                     'source_table_name': kwargs["source_table_name"],
    #                     'dest_connection_name': kwargs["dest_connection_name"],
    #                     'dest_table_name': kwargs['dest_table_name']
    #                     },
    #             pipe_ignore=step['pipe_ignore'],
    #             on_failure=print_error,)
    #         )
    #     pipeline(pipes).run()
    #     # pipeline_run(pk, pipes)

