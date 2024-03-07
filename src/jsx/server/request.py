from enum import Enum
from dataclasses import dataclass
from uuid import uuid4 as uuid


class RequestType(Enum):
    HTTP = "http"
    WS = "ws"


class Request:
    type: RequestType


@dataclass
class WSRequest(Request):
    type = RequestType.WS
    socket_id: str


@dataclass
class HTTPRequest(Request):
    type = RequestType.HTTP

    def __init__(self):
        self.id = str(uuid())


_request: WSRequest | HTTPRequest = None


def request():
    return _request


def set_request(request: Request):
    global _request
    _request = request
