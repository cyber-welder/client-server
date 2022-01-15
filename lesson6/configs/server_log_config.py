import logging
from logging.handlers import TimedRotatingFileHandler

LEVEL = logging.DEBUG

SERVER_LOGGER = logging.getLogger('server')

FILE_HANDLER = logging.handlers.TimedRotatingFileHandler(
                                    './lesson6/logs/log.log',
                                    encoding='utf-8',
                                    when='D',
                                    interval=1,
                                    backupCount=5)
FILE_HANDLER.setLevel(LEVEL)

FORMATTER = logging.Formatter("%(asctime)s | %(levelname)-10s | %(module)-12s | %(message)s ")
FILE_HANDLER.setFormatter(FORMATTER)

SERVER_LOGGER.addHandler(FILE_HANDLER)
SERVER_LOGGER.setLevel(LEVEL)
