import unittest
from fastapi.testclient import TestClient
from .server.asgi import app

class TestServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    @classmethod
    def tearDownClass(cls):
        cls.client.close()

    def test_index(self):
        response = TestServer.client.get("/c")
        self.assertEqual(response.status_code, 200)

