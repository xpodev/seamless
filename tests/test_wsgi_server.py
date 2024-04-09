import unittest
from .server.wsgi import app

class TestServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_index(self):
        response = TestServer.client.get("/c")
        self.assertEqual(response.status_code, 200)

