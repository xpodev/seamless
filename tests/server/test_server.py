from fastapi.testclient import TestClient
from . import app

client = TestClient(app)