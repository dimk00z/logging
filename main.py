# import logging
import logging.config
from setting import logger_config

logging.config.dictConfig(logger_config)
app_logger = logging.getLogger('app_logger')


def print_into_debug():

    app_logger.debug('Debug from print_into_debug()',
                     extra={'some': 'thing'})


def main():
    print_into_debug()

    app_logger.debug('Debug from main()', extra={'some': 'thing'})
    words = ['new house', 'apple', 'ice cream', 3]
    for item in words:
        try:
            1/0
            print(item.split(' '))
        except:
            app_logger.exception('Some', extra={'some': 'thing'})


if __name__ == "__main__":
    main()
