import json
import socket
import time
from argparse import ArgumentParser
from config import ENCODING, MAX_PACKAGE_LENGTH, PRESENCE, ACTION, TIME, ACCOUNT_NAME, RESPONSE


class Client:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.address, self.port))

    @staticmethod
    def status_presence(account_name='Guest'):
        return {ACTION: PRESENCE, TIME: time.time(), ACCOUNT_NAME: account_name}

    def get_answer(self):
        return json.loads(self.socket.recv(MAX_PACKAGE_LENGTH).decode(ENCODING))

    def send_message(self, message):
        if message == PRESENCE:
            message_to_server = json.dumps(self.status_presence())
        else:
            message_to_server = message
        self.socket.send(message_to_server.encode(ENCODING))
        return self.get_answer()


def main():
    parser = ArgumentParser()
    parser.add_argument('-a', help='address', type=str, default='localhost')
    parser.add_argument('-p', help='server port', type=int, default=7777)
    args = parser.parse_args()

    client_connect = Client(args.a, args.p)
    # client_connect.send_message(PRESENCE)
    client_connect.send_message('Сообщение')


if __name__ == "__main__":
    main()
