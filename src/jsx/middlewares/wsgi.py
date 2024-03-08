from socketio import Server, WSGIApp

from .base import BaseMiddleware
from ..server.request import set_request, HTTPRequest, request


class WSGIMiddleware(BaseMiddleware):
    def static_handler(self, env, start_response):
        http_path: str = env["PATH_INFO"]
        replace_path = f"{self.socket_path}/static/"
        file_path = self.STATIC_FOLDER / http_path.removeprefix(replace_path)

        if not file_path.exists():
            start_response("404 Not Found", [("Content-Type", "text/plain")])
            return [b"Not Found"]

        mime_type = self._mime_type(file_path.name)
        start_response("200 OK", [("Content-Type", mime_type)])

        with file_path.open("rb") as file:
            return [file.read()]

    def __call__(self, env, start_response):
        request = HTTPRequest.make(env)

        if request.method == "GET" and request.path.startswith(
            f"{self.socket_path}/static/"
        ):
            return self.static_handler(env, start_response)

        def c(status: str, headers: list, *args):
            headers.extend(self._make_cookie_header("_jsx_claimId", request.id))
            start_response(status, headers, *args)

        return self.app(env, c)

    def _app_class(self):
        return WSGIApp

    def _server_class(self):
        return Server
