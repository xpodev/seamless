from socketio import Server, WSGIApp

from .base import BaseMiddleware


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
        if env["REQUEST_METHOD"] == "GET" and env["PATH_INFO"].startswith(
            f"{self.socket_path}/static/"
        ):
            return self.static_handler(env, start_response)

        return self.app(env, start_response)

    def _app_class(self):
        return WSGIApp

    def _server_class(self):
        return Server
