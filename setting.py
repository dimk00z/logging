import logging


class MyFilter(logging.Filter):
    def filter(self, record):
        print(record.some)
        return record.funcName == 'print_into_debug'


class My_Handler(logging.Handler):
    def __init__(self, file_name):
        logging.Handler.__init__(self)
        self.file_name = file_name

    def emit(self, record):
        message = self.format(record)
        with open(self.file_name, 'a') as file:
            file.write(message+'\n')


format_string = '{asctime} - {levelname} - {name} - {module}:{funcName}:{lineno}- {message}'
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
            'formatter': 'std_formatter',
            'filters': ['my_filter']
        },
        'file_handler': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'std_formatter',
            'filename': 'debug.log'
        },
        'my_file_handler': {
            '()': My_Handler,
            'level': 'DEBUG',
            'formatter': 'std_formatter',
            'file_name': 'my_debug.log'
        },
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console_handler', 'file_handler', 'my_file_handler'],
            # 'propagate':False
        }
    },
    'filters': {
        'my_filter': {
            '()': MyFilter  # экземпляр класса
        }
    },
    # 'root': {}  # '':{}
    # 'incremental':True
}
