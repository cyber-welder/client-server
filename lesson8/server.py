import argparse
from modules.arg_types import ip_address, port
from loggers.server_log_config import SERVER_LOG
from modules.messenger import JimServer


def main():
    SERVER_LOG.debug('Application is started')
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=ip_address, default='localhost', dest='ip_addr')
    parser.add_argument('-p', type=port, default=7777, dest='port')
    args = parser.parse_args()
    my_server = JimServer(args.ip_addr, args.port, SERVER_LOG)
    my_server.listen()


if __name__ == '__main__':
    main()
