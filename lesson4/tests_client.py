import unittest

from lesson4.client import Client
from lesson4.config import MESSAGE


class TestClient(unittest.TestCase):

    def setUp(self):
        self.address = '127.0.0.1'
        self.port = 7777
        self.message = 'Сообщение'
        self.client = Client(self.address, self.port)

    def test_ip(self):
        result = get_ip(self.client)
        self.assertEqual(result, '127.0.0.1')

    def test_port(self):
        result = get_port(self.client)
        self.assertEqual(result, 7777)

    def test_answer(self):
        result = get_message(self.client, self.message)
        self.assertEqual(result[MESSAGE], 'Сообщение')

    def test_type_answer(self):
        result = get_message(self.client, self.message)
        self.assertEqual(type(result), dict)


def get_ip(client):
    return client.address


def get_port(client):
    return client.port


def get_message(client, message):
    return client.send_message(message)


if __name__ == "__main__":
    unittest.main()
