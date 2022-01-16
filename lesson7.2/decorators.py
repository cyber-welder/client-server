from configs.server_log_config import SERVER_LOGGER
from configs.client_log_config import CLIENT_LOGGER
import inspect


def log_server(func):
    def log_saver(*args, **kwargs):
        ret = func(*args, **kwargs)
        SERVER_LOGGER.debug(f'Функция {func.__name__} вызвана из функции {inspect.stack()[1][3]}')
        return ret
    return log_saver


def log_client(func):
    def log_saver(*args, **kwargs):
        ret = func(*args, **kwargs)
        CLIENT_LOGGER.debug(f'Функция {func.__name__} вызвана из функции {inspect.stack()[1][3]}')
        return ret
    return log_saver
