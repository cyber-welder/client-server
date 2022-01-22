import sys
import argparse
import time
import threading

from modules.arg_types import ip_address, port
from modules.messenger import JimClient
from loggers.client_log_config import CLIENT_LOG
from modules.constants import *


def sending(client):
    while True:
        recipient = input('Введите получателя или\n-all отправить всем\n'
                          '-exit отключиться и выйти\n: ')
        if recipient == '-exit':
            break
        elif recipient == '':
            print('Получатель не должен быть пустым.')
            continue
        text = input('Message: ')
        if text == '':
            print('Сообщение не должно быть пустым.')
            continue
        if recipient == '-all':
            client.send_to_all(text)
        else:
            client.send_message(recipient, text)


def listening(client):
    while client.active_session:
        client.listen()


def main():
    CLIENT_LOG.debug('Программа запущена')
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'user',
        type=str,
        help='Тестово допустимые имена: , user-1, user-2, user-3 и user-4',
    )
    parser.add_argument('ip_addr', type=ip_address, nargs='?', default='localhost')
    parser.add_argument('port', type=port, nargs='?', default=7777)
    args = parser.parse_args()

    my_client = JimClient(args.ip_addr, args.port, CLIENT_LOG)
    my_client.connect()
    if my_client.send_presence(args.user, 'Online') != OK200:
        print(f'Пользователь {args.user} не смог подключиться к серверу')
        sys.exit()

    print(f'Клиент зарегистрирован как {args.user}.')

    listening_thread = threading.Thread(target=listening, args=(my_client,), daemon=True)
    sending_thread = threading.Thread(target=sending, args=(my_client,), daemon=True)
    listening_thread.start()
    sending_thread.start()

    while True:
        time.sleep(1)
        if not (listening_thread.is_alive() and sending_thread.is_alive()):
            break

    my_client.disconnect()


if __name__ == '__main__':
    main()
