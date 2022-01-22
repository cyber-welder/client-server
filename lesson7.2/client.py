import json
import socket
import time
from configs.config import ENCODING, MAX_PACKAGE_LENGTH, PRESENCE, ACTION, TIME, ACCOUNT_NAME, RESPONSE
from configs.client_log_config import CLIENT_LOGGER
from decorators import log_client


class Client:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.address, self.port))
        CLIENT_LOGGER.info(f'Отправлен запрос на подключение пользователя - {self.address}:{self.port}')

    @log_client
    def status_presence(self, account_name='Guest'):
        return {ACTION: PRESENCE, TIME: time.time(), ACCOUNT_NAME: account_name}

    @log_client
    def get_answer(self):
        answer = json.loads(self.socket.recv(MAX_PACKAGE_LENGTH).decode(ENCODING))
        CLIENT_LOGGER.info(f'Ответ сервера получен. Код: {answer[RESPONSE]}')
        return answer

    @log_client
    def send_message(self, message):
        if message == PRESENCE:
            message_to_server = json.dumps(self.status_presence())
        else:
            message_to_server = message
        self.socket.send(message_to_server.encode(ENCODING))
        CLIENT_LOGGER.info('Отправлено сообщение на сервер')
        return self.get_answer()

    def send(self, m='echo'):
        self.socket.send(m.encode(ENCODING))

    def get(self):
        return self.socket.recv(MAX_PACKAGE_LENGTH).decode(ENCODING)
