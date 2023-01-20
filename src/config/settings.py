import os
from src.config.env import env, environ, BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
# ------------------------------------------------------------------------------
# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'jazzmin',
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
DATABASES: dict = {
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
        "NAME": "arm_dbk1",
        "USER": None,
        "PASSWORD": None,
        # "HOST": "dbk1.ntbroker.ru\\s2005",
        "HOST": f"{DOMAIN}",
        # "PORT": "1433",
        "OPTIONS": {"driver": "SQL Server Native Client 11.0", "extra_params": "TrustServerCertificate=Yes;"},
    },
    "gtd_arm_test": {
        "ENGINE": "mssql",
        "NAME": "gtd_0_arm_2022_dbk1",
        "USER": None,
        "PASSWORD": None,
        # "HOST": "dbk1.ntbroker.ru\s2005",
        "HOST": f"{DOMAIN}",
        "PORT": "1433",
        "OPTIONS": {"driver": "SQL Server Native Client 11.0",
                    "extra_params": "TrustServerCertificate=Yes;",
                    },
    },
    "dbf_2022_test": {
        "ENGINE": "src.db.connection.advantage",
        # "NAME": "E:\\MyDocuments\\FoxProProjects\\Bastion\\BASE\\GTD_2022_LG\\GTD_2022_LG.add",
        # "NAME": "\\\\10.1.0.12\\K\\softland\\BASE\\GTD_2022_BOROD",
        # "NAME": f"\\\\{DOMAIN}\\FTSBASES\\TEST",
        "NAME": f"\\\\{DOMAIN}\\FTSBASES\\GTD_2022_DOMODEDOVO",
        # "NAME": f"\\\\{DOMAIN}\\FTSBASES\\GTD_2022_LG",
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
        # "NAME": "test",
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

PROJECT_ROOT = environ.Path(__file__) - 3

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'

# https://pythobyte.com/serving-static-files-in-python-with-django-aws-s3-and-whitenoise-aaff3e61/
# Настройка Статических файлов
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles-cdn')

STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)

# Extra lookup directories for collectstatic to find static files
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
################################################################################
# REDIS
################################################################################
REDIS_HOST = env.str('REDIS_HOST')
REDIS_PORT = env.int('REDIS_PORT')
################################################################################
# CACHE settings
################################################################################
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f"redis://{REDIS_HOST}:{REDIS_PORT}/1",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        "KEY_PREFIX": "dbf2mssql",
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
# Cache time to live is 15 minutes
# CACHE_TTL = 60 * 15
################################################################################
# LOGGING settings
################################################################################
from src.config.loggers import *
################################################################################
# Django show Toolbar
################################################################################
# def show_toolbar(request):
#     # is no ajax
#     if not request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' \
#             and request.user \
#             and request.user.is_authenticated \
#             and request.user.is_superuser \
#             and env.bool('SHOW_DEBUG_TOOLBAR', default=False):
#         return True
#     return False
################################################################################
# Django Debug Toolbar
################################################################################
if DEBUG:
    INTERNAL_IPS = ['127.0.0.1', '192.168.89.213', ]
    INSTALLED_APPS.extend(["debug_toolbar", "django_extensions"])
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda _: False}

if not DEBUG:
    MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TOOLBAR_CALLBACK': 'src.config.settings.show_toolbar'
# }
################################################################################
# UPDATE DATABASES dict from connects table !
################################################################################
# See also: Update database script added to WSGI.py !
################################################################################
# DRAMATIQ settings
################################################################################
from src.config.dramatiq import *
################################################################################
# Import django-jazzmin settings
################################################################################
from src.config.jazzmin import JAZZMIN_SETTINGS
################################################################################
# Import EMAIL settings
################################################################################
from src.config.email import *
