format_string = '{asctime} - {levelname} - {name} - {message}'
logger_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'std_formatter': {
            'format': format_string,
            'style': '{'
        }
    },
    'handlers': {
        'console_handler': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_formatter'
        },
        'file_handler': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'std_formatter',
            'filename': 'debug.log'
        },
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console_handler', 'file_handler'],
            # 'propagate':False
        }
    },
    # 'filters': {},
    # 'root': {}  # '':{}
    # 'incremental':True
}
