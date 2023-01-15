import os
from django.conf import settings
from celery import Celery

# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.config.settings")

app = Celery("tasks")

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object("django.conf:settings", namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Start celery
# celery worker -A src.services.tasks --loglevel=info -P eventlet -E
# celery worker -A src.services.tasks --loglevel=info -E --pool=solo
# celery worker -A src.services.tasks -B --loglevel=info -E --pool=gevent --concurrency=50

# celery worker -A src.services.tasks --loglevel=info -E --pool=gevent --concurrency=4
# celery worker -A src.services.tasks --loglevel=info -E --pool=solo --concurrency=4

################################################################################
# CELERY_ NAMESPACE
################################################################################
# CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
# CELERY_BROKER_TRANSPORT_OPTIONS={'visibility_timeout': 3600}
# CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
#
# CELERY_RESULT_EXTENDED = True
