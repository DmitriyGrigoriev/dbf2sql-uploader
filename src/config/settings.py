import redis
import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Load operating system environment variables and then prepare to use them
env = environ.Env()
# reading .env file ~/projects/broker/config/.env
environ.Env.read_env(BASE_DIR + '/config/.env' )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
# ------------------------------------------------------------------------------
# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'django_dramatiq',
    'import_export',
]

LOCAL_APPS = [
    'src.apps.core.apps.CoreConfig',
    'src.apps.sqlimport.apps.SqlimportConfig',
    'src.apps.dbfexport.apps.DbfexportConfig',
    'src.apps.armimport.apps.ArmimportConfig',
    'src.apps.armexport.apps.ArmexportConfig',
    'src.apps.task_scheduler.apps.TaskSchedulerConfig',
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
################################################################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
################################################################################
DEBUG = env.bool('DEBUG')
SECRET_KEY = env.str('SECRET_KEY')
# DOMAINS ######################################################################
DOMAIN = env.str('DOMAIN')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', )

SITE_ID = 1
ROOT_URLCONF = 'src.config.urls'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "apps/../services/templates")
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.config.wsgi.application'

################################################################################
# Database SQLLite3
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
################################################################################
DATABASE_DIR = os.path.join(BASE_DIR, 'db')

################################################################################
# Database MSSQL (required installed package mssql-django)
################################################################################
DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": "UPLOADER",
        "USER": None,
        "PASSWORD": None,
        "HOST": f"{DOMAIN}",
        "PORT": "1433",
        # "Trusted_Connection": "no",
        "OPTIONS": {"driver": "SQL Server Native Client 11.0",
                    "extra_params": "TrustServerCertificate=Yes; Trusted_Connection=Yes",
                    },
    },
    "localfts": {
        "ENGINE": "mssql",
        "NAME": "LocalFts",
        "USER": None,
        "PASSWORD": None,
        "HOST": "localhost",
        # "HOST": f"{DOMAIN}",
        "PORT": "1433",
        "OPTIONS": {"driver": "SQL Server Native Client 11.0",
                    "extra_params": "TrustServerCertificate=Yes; Trusted_Connection=Yes",
                    },
    },
    "arm_edh": {
        "ENGINE": "mssql",
        # "NAME": "arm_dbk1",
        "NAME": "arm_edh1",
        "USER": None,
        "PASSWORD": None,
        # "HOST": "dbk1.ntbroker.ru\\s2005",
        "HOST": f"{DOMAIN}",
        # "PORT": "1433",
        "OPTIONS": {"driver": "SQL Server Native Client 11.0", "extra_params": "TrustServerCertificate=Yes;"},
    },
    "gtd_arm_test": {
        "ENGINE": "mssql",
        # "NAME": "gtd_0_arm_2022_dbk1",
        "NAME": "gtd_arm_2022",
        "USER": None,
        "PASSWORD": None,
        # "HOST": "dbk1.ntbroker.ru\s2005",
        "HOST": f"{DOMAIN}",
        "PORT": "1433",
        "OPTIONS": {"driver": "SQL Server Native Client 11.0",
                    "extra_params": "TrustServerCertificate=Yes;",
                    },
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(DATABASE_DIR, 'uploader.db'),
    #     "OPTIONS": {"timeout": 10},
    # },
    "dbf_2022_borod_test": {
        "ENGINE": "src.db.connection.advantage",
        # "NAME": "E:\\MyDocuments\\FoxProProjects\\Bastion\\BASE\\GTD_2022_LG\\GTD_2022_LG.add",
        # "NAME": "\\\\10.1.0.12\\K\\softland\\BASE\\GTD_2022_BOROD",
        # "NAME": f"\\\\{DOMAIN}\\FTSBASES\\TEST",
        "NAME": f"\\\\{DOMAIN}\\FTSBASES\\GTD_2022_BOROD",
        "USER": "",
        "PASSWORD": "",
        # "AUTOCOMMIT": True,
        "OPTIONS": {"driver": "Advantage StreamlineSQL ODBC",
                    "setdecoding": {"encoding": "cp866"},
                    "extra_params": "ServerTypes=1;"
                    },
        # "OPTIONS": {"dsn": "Clipper",},
        # "OPTIONS": {"driver": "Advantage ODBC Driver",
        #             "setdecoding": {"encoding": "cp1251"},
        # },
        # "OPTIONS": {"driver": "/opt/ads/odbc/redistribute/x64/libadsodbc.so",
        #             # "setdecoding": {"encoding": "cp1251"},
        # },
    },
    "test": {
        "ENGINE": "mssql",
        "NAME": "test",
        "USER": None,
        "PASSWORD": None,
        "HOST": f"{DOMAIN}",
        "PORT": "1433",
        "Trusted_Connection": "yes",
        "OPTIONS": {"driver": "SQL Server Native Client 11.0",},
        # "OPTIONS": {"driver": "ODBC Driver 18 for SQL Server", "extra_params": "TrustServerCertificate=Yes; Trusted_Connection=Yes"},
        # "OPTIONS": {"driver": "ODBC Driver 18 for SQL Server", "extra_params": "TrustServerCertificate=Yes",},
    },
}
################################################################################
# Database PostgreeSQL
################################################################################
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'db_name',
#         'USER': 'dbms',
#         'PASSWORD': 'db_password',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

PROJECT_ROOT = ROOT_DIR = environ.Path(__file__) - 3

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
################################################################################
# SECTION: export / import
################################################################################
# Path to the connection module for customs data sources
CONNECTION_MODULE = 'src.db.connection.connects'
PIPE_MODULES = {
    'DBF': {
        'export': 'src.apps.dbfexport',
        'import': 'src.apps.sqlimport',
        'resource': 'resources', # module: resources.py
        'table_prefix': 'T'
    },
    'ARM': {
        'export': 'src.apps.armexport',
        'import': 'src.apps.armimport',
        'resource': 'resources', # module: resources.py
        'table_prefix': ''
    },
}
CONNECTION_FTS = 'localfts'
ONE_HOUR = 3600000
################################################################################
# REDIS
################################################################################
REDIS_HOST = env.str('REDIS_HOST')
REDIS_PORT = env.int('REDIS_PORT')
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
        # This middleware stores metadata about tasks in flight to a database and exposes them via the Django admin.
        "django_dramatiq.middleware.AdminMiddleware",
        # This middleware stores message_id in the ImportTables.message_id field
        "src.services.middleware.ImportTablesAdminMiddleware",
        # This middleware is vital in taking care of closing expired connections after each message is processed.
        "django_dramatiq.middleware.DbConnectionsMiddleware",
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
        "result_ttl": ONE_HOUR
    }
}
# DRAMATIQ_AUTODISCOVER_MODULES = []
################################################################################
# Defines which database should be used to persist Task objects when the
# AdminMiddleware is enabled.  The default value is "default".
DRAMATIQ_TASKS_DATABASE = "default"
################################################################################
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
}

################################################################################
# UPDATE DATABASES dict from connects table !
################################################################################
# See also: Update database script added to WSGI.py !