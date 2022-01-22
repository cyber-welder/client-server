from argparse import ArgumentParser
from client import Client


def main():
    parser = ArgumentParser()
    parser.add_argument('-a', help='address', type=str, default='localhost')
    parser.add_argument('-p', help='server port', type=int, default=7777)
    args = parser.parse_args()

    client_connect = Client(args.a, args.p)
    client_connect.send(f'Сообщение отправляющего пользователя ')


if __name__ == "__main__":
    main()
