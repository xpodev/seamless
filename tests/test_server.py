import unittest
from fastapi.testclient import TestClient
from .server import app

client = TestClient(app)


class TestServer(unittest.TestCase):
    def test_index(self):
        response = client.get("/c")
        self.assertEqual(response.status_code, 200)

    def test_static(self):
        response = client.get("/socket.io/static/main.js")
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.headers["content-type"], ["application/javascript", "text/javascript"])
