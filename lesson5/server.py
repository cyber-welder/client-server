import socket
import json
from argparse import ArgumentParser
from config import MAX_CONNECTIONS, MAX_PACKAGE_LENGTH, ENCODING, ERROR, MESSAGE, RESPONSE
from log.server_log_config import SERVER_LOGGER


class Server:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.address, self.port))

    def start_server(self):
        self.socket.listen(MAX_CONNECTIONS)
        SERVER_LOGGER.info(f'Сервер запущен. host: "{self.address}", port: {self.port}')
        while True:
            client, client_address = self.socket.accept()
            SERVER_LOGGER.info(f'Подключен клиент: {self.address}:{self.port}')
            try:
                message_from_client = client.recv(MAX_PACKAGE_LENGTH).decode(ENCODING)
                message_to_client = self.processing_client_message(message_from_client)
            except BaseException:
                message_to_client = self.processing_client_message(ERROR)
                client.close()

            client.send(json.dumps(message_to_client).encode(ENCODING))
            client.close()

    @staticmethod
    def processing_client_message(message):
        if message == ERROR:
            SERVER_LOGGER.warning(f'Получено сообщение от клиента. Код: {400}')
            return {MESSAGE: message, RESPONSE: 400}
        SERVER_LOGGER.info(f'Получено сообщение от клиента. Код: {200}')
        return {MESSAGE: message, RESPONSE: 200}


def main():
    parser = ArgumentParser()
    parser.add_argument('-a', help='address', type=str, default='localhost')
    parser.add_argument('-p', help='server port', type=int, default=7777)
    args = parser.parse_args()

    server = Server(args.a, args.p)
    server.start_server()


if __name__ == '__main__':
    main()
