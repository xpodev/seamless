from enum import Enum
from dataclasses import dataclass
from uuid import uuid4 as uuid
from urllib.parse import parse_qs

from jsx.internal import Cookies


class RequestType(Enum):
    HTTP = "http"
    WS = "ws"


class Request:
    type: RequestType

    @classmethod
    def make(cls, request_data, **kwargs):
        request = cls(request_data, **kwargs)
        set_request(request)
        return request


@dataclass
class WSRequest(Request):
    type = RequestType.WS
    socket_id: str


class HTTPRequest(Request):
    type = RequestType.HTTP
    path: str
    method: str
    query: dict[str, str | list[str]]
    headers: dict
    cookies: Cookies

    id: str = None

    def __init__(self, raw_request: dict, *, type=None):
        self._raw_request = raw_request
        if type == "asgi" or "asgi" in raw_request:
            self._parse_asgi()
        else:
            self._parse_wsgi()

    def _parse_headers(self, headers: dict):
        return {k.decode(): v.decode() for k, v in headers}

    def _parse_query(self, query_string: str):
        self._raw_query = query_string
        return {
            k.decode(): v[0].decode() if len(v) == 1 else [i.decode() for i in v]
            for k, v in parse_qs(query_string).items()
        }

    def _parse_asgi(self):
        self.method = self._raw_request["method"]
        self.path = self._raw_request["path"]
        self.query = self._parse_query(self._raw_request["query_string"])
        self.headers = self._parse_headers(self._raw_request["headers"])
        self.cookies = Cookies.from_request_headers(self.headers)

    def _parse_wsgi(self):
        self.method = self._raw_request["REQUEST_METHOD"]
        self.path = self._raw_request["PATH_INFO"]
        self.query = self._parse_query(self._raw_request["QUERY_STRING"])
        self.headers = {
            k: v for k, v in self._raw_request.items() if k.startswith("HTTP_")
        }
        self.cookies = Cookies.from_request_headers(self.headers)

    @property
    def full_path(self):
        return f"{self.path}?{self._raw_query}"
    

_request: WSRequest | HTTPRequest = None


def request():
    return _request


def set_request(request: Request):
    global _request
    _request = request
