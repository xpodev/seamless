from enum import Enum
from dataclasses import dataclass
from urllib.parse import parse_qs

from seamless.internal import Cookies


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
        self._parse()

    def _parse_headers(self, headers: dict):
        return {k.decode(): v.decode() for k, v in headers}

    def _parse_query(self, query_string: str):
        self._raw_query = query_string
        return {
            k: v[0] if len(v) == 1 else [i for i in v]
            for k, v in parse_qs(query_string).items()
        }

    def _parse(self):
        self.method = self._raw_request["method"]
        self.path = self._raw_request["path"]
        self.query = self._parse_query(self._raw_request["query_string"])
        self.headers = self._parse_headers(self._raw_request["headers"])
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
