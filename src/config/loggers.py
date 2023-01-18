import os
from src.config.settings import PROJECT_ROOT

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s|%(asctime)s|%(module)s|%(process)d|%(thread)d|%(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'rich': {
            'datefmt': "[%X]"
        },
    },
    'handlers': {
        'console': {
            'class': 'rich.logging.RichHandler',
            # 'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(PROJECT_ROOT, 'debug.log'),
            'formatter': 'verbose',
            'when': 'midnight',
            'backupCount': '30',
        },
        # 'file': {
        #     'level': 'DEBUG',
        #     # 'class': 'logging.FileHandler',
        #     'class': 'logging.handlers.TimedRotatingFileHandler',
        #     'maxBytes': 1024 * 1024 * 5,  # 5 MB
        #     'backupCount': 5,
        #     'formatter': 'verbose',
        #     # 'formatter': 'file',
        #     'filename': os.path.join(PROJECT_ROOT, 'debug.log'),
        #     'when': 'midnight',
        #     # 'filename': 'debug.log'
        # }
    },
    'loggers': {
        # '': {
        #     'level': 'DEBUG',
        #     'handlers': ['console', 'file']
        # },
        '': {
            'handlers': ['console','default'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}