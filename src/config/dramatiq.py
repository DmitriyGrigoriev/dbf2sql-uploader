import os
import redis
from src.config.env import env
from src.apps.common.dataclasses import ETL

################################################################################
# REDIS
################################################################################
REDIS_HOST = env.str('REDIS_HOST')
REDIS_PORT = env.int('REDIS_PORT')

################################################################################
# DRAMATIQ
################################################################################
DRAMATIQ_REDIS_URL = os.getenv("REDIS_URL", f"redis://{REDIS_HOST}:{REDIS_PORT}/0")
DRAMATIQ_BROKER = {
    "BROKER": "dramatiq.brokers.redis.RedisBroker",
    "OPTIONS": {
        "connection_pool": redis.ConnectionPool.from_url(DRAMATIQ_REDIS_URL),
    },
    "MIDDLEWARE": [
        "dramatiq.middleware.AgeLimit",
        "dramatiq.middleware.TimeLimit",
        # Middleware that lets you chain success and failure callbacks onto Actors.
        "dramatiq.middleware.Callbacks",
        "dramatiq.middleware.Retries",
        "dramatiq.middleware.Pipelines",
        # This middleware stores metadata about tasks in flight to a database and exposes them via the Django admin.
        "django_dramatiq.middleware.AdminMiddleware",
        # This middleware is vital in taking care of closing expired connections after each message is processed.
        "django_dramatiq.middleware.DbConnectionsMiddleware",
        # This middleware stores message_id in the ImportTables.message_id field
        "src.services.middleware.ImportTablesAdminMiddleware",
    ]
}
# from django_dramatiq.middleware import AdminMiddleware
# from django_dramatiq.models import Task
DRAMATIQ_RESULT_BACKEND = {
    "BACKEND": "dramatiq.results.backends.redis.RedisBackend",
    "BACKEND_OPTIONS": {
        "url": f"redis://{REDIS_HOST}:{REDIS_PORT}",
    },
    "MIDDLEWARE_OPTIONS": {
        # The maximum number of milliseconds results areallowed to exist in the backend
        "result_ttl": ETL.TIMELMIT.ONE_HOUR
    }
}
# DRAMATIQ_AUTODISCOVER_MODULES = []
################################################################################
# Defines which database should be used to persist Task objects when the
# AdminMiddleware is enabled.  The default value is "default".
DRAMATIQ_TASKS_DATABASE = "default"
################################################################################
