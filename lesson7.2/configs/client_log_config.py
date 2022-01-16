import logging
from logging.handlers import TimedRotatingFileHandler

LEVEL = logging.DEBUG

CLIENT_LOGGER = logging.getLogger('client')

FILE_HANDLER = logging.handlers.TimedRotatingFileHandler(
                                    './lesson7.2/logs/log.log',
                                    encoding='utf-8',
                                    when='D',
                                    interval=1,
                                    backupCount=5)
FILE_HANDLER.setLevel(LEVEL)

FORMATTER = logging.Formatter("%(asctime)s | %(levelname)-10s | %(module)-12s | %(message)s ")
FILE_HANDLER.setFormatter(FORMATTER)

CLIENT_LOGGER.addHandler(FILE_HANDLER)
CLIENT_LOGGER.setLevel(LEVEL)
