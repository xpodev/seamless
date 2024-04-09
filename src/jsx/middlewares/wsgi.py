from socketio import Server, WSGIApp

from .base import BaseMiddleware, CLAIM_COOKIE_NAME
from ..server.request import HTTPRequest


class WSGIMiddleware(BaseMiddleware):
    def __call__(self, env, start_response):
        request = HTTPRequest.make(env)

        def _start_response(status: str, headers: list, *args):
            headers.extend(self._make_cookie_header(CLAIM_COOKIE_NAME, request.id))
            start_response(status, headers, *args)

        return self.app(env, _start_response)

    def _app_class(self):
        return WSGIApp

    def _server_class(self):
        return Server
