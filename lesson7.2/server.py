import socket
import json
from select import select
from argparse import ArgumentParser
from configs.config import MAX_CONNECTIONS, MAX_PACKAGE_LENGTH, ENCODING, ERROR, MESSAGE, RESPONSE
from configs.server_log_config import SERVER_LOGGER
from decorators import log_server


class Server:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.clients = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.address, self.port))
        self.socket.listen(MAX_CONNECTIONS)
        # self.socket.settimeout(5)

    @log_server
    def start_server(self):
        SERVER_LOGGER.info(f'Сервер запущен. host: "{self.address}", port: {self.port}')
        while True:
            try:
                client, client_address = self.socket.accept()
                SERVER_LOGGER.info(f'Подключен клиент: {client_address}')
            except Exception as e:
                print(f'{e}')
                SERVER_LOGGER.info(f'Ошибка подключения клиента: {client_address}')
            else:
                self.clients.append(client)
            finally:
                try:
                    r, w, e = select(self.clients, self.clients, [], 10)
                    message_to_client = f'{client.recv(MAX_PACKAGE_LENGTH).decode(ENCODING)} {client.fileno()} {client.getpeername()}'
                    SERVER_LOGGER.info(f'Получено сообщение: {message_to_client} от клиента: {client.fileno()} {client.getpeername()}')
                    for c in w:
                        c.send(message_to_client.encode(ENCODING))
                        SERVER_LOGGER.info(f'Сообщение: "{message_to_client}" отправлено клиенту: {c.fileno()} {c.getpeername()}')
                except Exception as e:
                    print(f'{e}')

    @log_server
    def processing_client_message(self, message):
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
