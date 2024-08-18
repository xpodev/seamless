from ..context.context import Context, get_context
from ..context.request import request as _request


class BaseMiddleware:
    def __init__(self, app, socket_path="/socket.io", context: Context | None = None):
        if context is None:
            context = get_context()
        self.socket_path = f"/{socket_path.strip('/')}"
        self.app = self._app_class()(context.server, app, socketio_path=socket_path)

    def _app_class(self):
        raise NotImplementedError("self._app_class is not implemented")

    def _make_cookie_header(
        self,
        name: str,
        value,
        *,
        expires: str | None = None,
        path: str | None = None,
        http_only: bool | None = None,
        domain: str | None = None,
        same_site: str | None = None,
        max_age: int | None = None,
        secure: bool | None = None,
    ):
        if path is None:
            path = self.socket_path
        cookie_value = f"{name}={value};"
        if max_age:
            cookie_value += f" Max-Age={max_age};"
        if expires:
            cookie_value += f" Expires={expires};"
        if path:
            cookie_value += f" Path={path};"
        if domain:
            cookie_value += f" Domain={domain};"
        if secure:
            cookie_value += " Secure;"
        if http_only:
            cookie_value += " HttpOnly;"
        if same_site:
            cookie_value += f" SameSite={same_site};"

        return (b"Set-Cookie", cookie_value.encode())

    def _remove_cookie(self, name: str, path: str | None = None):
        if path is None:
            path = self.socket_path
        return (
            b"Set-Cookie",
            f"{name}=; Path={path}; Expires=Thu, 01 Jan 1970 00:00:00 GMT;".encode(),
        )

    def _is_render_request(self):
        request = _request()
        if not request:
            return False
        return request.id is not None
