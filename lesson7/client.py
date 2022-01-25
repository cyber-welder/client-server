import re

import logs.config.client_config_log
import argparse
import logging
import decorators
from datetime import datetime
import pickle

import socket
from config import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    OK, server_port, server_address, StandartServerCodes, UnknownCode

log = logging.getLogger('Client_log')
logger = decorators.Log(log)


@logger
def create_presence_message(user_name):
    log.info('Формирование сообщения')
    if len(user_name) > 25:
        log.error('Имя пользователя более 25 символов!')
        raise ValueError

    if not isinstance(user_name, str):
        log.error('Полученное имя пользователя не является строкой символов')
        raise TypeError

    message = {
        ACTION: PRESENCE,
        TIME: datetime.today().strftime("%Y-%m-%d-%H.%M.%S"),
        USER: {
            ACCOUNT_NAME: user_name
        }
    }
    return message


def send_message(m):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if server_address != '0.0.0.0':
        s.connect((server_address, server_port))
    else:
        s.connect(('localhost', server_port))

    message = create_presence_message(user_name)
    if isinstance(message, dict):
        data_string = pickle.dumps(message)

    print(f'Отправляю сообщение "{message}" на сервер')

    s.send(m.encode('utf-8'))


@logger
def start_client(user_name):
    log.info('Запуск клиента')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if server_address != '0.0.0.0':
        s.connect((server_address, server_port))
    else:
        s.connect(('localhost', server_port))

    message = create_presence_message(user_name)
    if isinstance(message, dict):
        data_string = pickle.dumps(message)

    log.info(f'Отправляю сообщение "{message}" на сервер')

    s.send(data_string)
    log.info('жду ответа')

    data_bytes = s.recv(1024)
    server_response = pickle.loads(data_bytes)
    log.info('Ответ:', server_response)
    if server_response.get('response') not in StandartServerCodes:
        log.error(f'Неизвестный код ответа от сервера: {server_response.get("response")}')
        s.close()
        raise UnknownCode(server_response.get('response'))
    if server_response.get('response') == OK:
        log.info('Сервер OK!')
    else:
        log.error('Ошибка сервера!')
    s.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, help='Port server', default=server_port)
    parser.add_argument('-a', '--address', type=str, help='Address server', default=server_address)
    parser.add_argument('-u', '--user', type=str, help='User name', default='Guest')

    args = parser.parse_args()

    server_port = args.port
    server_address = args.address
    user_name = args.user

    start_client(user_name)
