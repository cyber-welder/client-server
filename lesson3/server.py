from argparse import ArgumentParser
from socket import socket, AF_INET, SOCK_STREAM

parser = ArgumentParser()
parser.add_argument('--port', help='server port', type=int, default=7777)
parser.add_argument('--addr', help='address', type=str, default='')
args = parser.parse_args()

server = socket(AF_INET, SOCK_STREAM)
server.bind((args.addr, args.port))
server.listen(5)
print(f'Сервер запущен. host: "{args.addr}", port: {args.port}')

while True:
    client, addr = server.accept()
    print(f'Входящее соединение с IP: {addr}')
    data = client.recv(1024)
    print(f'Полученное сообщение: {data.decode(encoding="utf-8")}')
    data = ('<Обработано сервером>' + data.decode(encoding="utf-8") + '<Обработано сервером>').encode('utf-8')
    client.send(data)
    print('Ответ отправлен')
    client.close()
