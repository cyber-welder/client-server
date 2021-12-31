import unittest
from lesson4.server import Server


class TestServer(unittest.TestCase):

    def setUp(self):
        self.address = '127.0.0.1'
        self.port = 7777
        self.server = Server(self.address, self.port)

    def test_ip(self):
        result = get_ip(self.server)
        self.assertEqual(result, '127.0.0.1')

    def test_port(self):
        result = get_port(self.server)
        self.assertEqual(result, 7777)


def get_ip(server):
    return server.address


def get_port(server):
    return server.port


if __name__ == "__main__":
    unittest.main()
