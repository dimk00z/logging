# import logging
import logging.config
from setting import logger_config

logging.config.dictConfig(logger_config)
app_logger = logging.getLogger('app_logger')


def main():
    app_logger.debug(f'Enter in to the main()')


if __name__ == "__main__":
    main()
