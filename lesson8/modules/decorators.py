# from functools import wraps
import re
from traceback import extract_stack, format_list


def log(func):
    def wrapper(self, *args, **kwargs):
        pattern = re.compile(r'(?a)File "[^"]+", (line \d+), in (\S+)\s')

        match = pattern.search(format_list(extract_stack(limit=2))[0])
        if match:
            self._logger.debug(f'Функция <{func.__name__}> вызвана из '
                               f'функции <{match.group(2)}> '
                               f'({match.group(1)}) с '
                               f'параметрами {args}')
        else:
            self._logger.debug(f'Функция <{func.__name__}> вызвана '
                               f'с параметрами {args}')
        result = func(self, *args, **kwargs)
        if func.__name__ == 'error_response':
            err_code = args[1]
            err_message = args[2]
            self._logger.error(f'{err_code}: {err_message}')
        elif func.__name__ == 'ok_response':
            answer_code = args[1]
            message = args[2] if len(args) == 3 else ''
            self._logger.info(f'{answer_code}: {message}')
        return result
    return wrapper
