from functools import wraps
from mimetypes import guess_type
from pathlib import Path
from inspect import iscoroutinefunction

import asyncio

from socketio.base_server import BaseServer
from socketio import AsyncServer

from ..server.database import DB
from ..server.ws_router import ws_router
from ..server.request import WSRequest, request as _request

from ..internal import Cookies


class BaseMiddleware:
    STATIC_FOLDER = Path(__file__).parent.parent / "server/static"

    def __init__(self, app, socket_path="/socket.io"):
        self.socket_path = f"/{socket_path.strip('/')}"
        self.server = self._server_class()(cors_allowed_origins=[])
        self.app = self._app_class()(self.server, app, socketio_path=socket_path)
        self._disconnect = self._make_method(self.server.disconnect)
        self._setup()

    def _setup(self):
        self._setup_events()

    def _emit(self, *args, **kwargs):
        return self.server.emit(*args, **kwargs)

    def _setup_events(self):
        self.server.on("disconnect", self._handle_disconnect)
        self.server.on("connect", self._handle_connect)
        self.on("dom_event", self._make_method(self.dom_event))

        for command, handler in ws_router.items():
            self.on(command, self._make_handler(handler))

    def _make_handler(self, handler):
        def _handler(sid, *data):
            result = handler(sid, *data)
            if result is None:
                return

            response_event, *response_data = result
            self._emit(response_event, *response_data, to=sid)

        return _handler

    def dom_event(self, sid, data: str, event_data):
        component_id, event = data.split(":")
        try:
            DB.invoke_element_event(component_id, sid, event, event_data)
        except KeyError:
            raise Exception(
                f"Element {component_id} not found"
            )

    def _handle_disconnect(self, sid: str):
        DB.release_elements(sid)
    def _handle_connect(self, sid: str, env):
        cookie_string = env.get("HTTP_COOKIE", "")
        if not cookie_string:
            self._disconnect(sid)

        cookies = Cookies(env.get("HTTP_COOKIE", ""))
        claim_id = cookies["_jsx_claimId"]
        if not claim_id:
            self._disconnect(sid)

        DB.claim_http_elements(claim_id, sid)

    def on(self, event, handler):
        @wraps(handler)
        def wrapper(sid, *args, **kwargs):
            try:
                WSRequest.make(sid)
                return handler(sid, *args, **kwargs)
            except Exception as e:
                self._emit("error", str(e), to=sid)

        self.server.on(event, wrapper)

    def _mime_type(self, filename: str):
        mime_type, _ = guess_type(filename)
        return mime_type or "text/plain"

    def _app_class(self):
        raise NotImplementedError("self._app_class is not implemented")

    def _server_class(self) -> type[BaseServer]:
        raise NotImplementedError("self._server_class is not implemented")

    def _is_async_server(self) -> bool:
        return False

    def _make_cookie_header(
        self,
        name: str,
        value,
        *,
        expires: str = None,
        path: str = None,
        http_only: bool = None,
        domain: str = None,
        same_site: str = None,
        max_age: int = None,
        secure: bool = None,
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

        return [(b"Set-Cookie", cookie_value.encode())]

    def _remove_cookie(self, name: str, path: str = None):
        if path is None:
            path = self.socket_path
        return [
            (
                b"Set-Cookie",
                f"{name}=; Path={path}; Expires=Thu, 01 Jan 1970 00:00:00 GMT;".encode(),
            )
        ]

    def _make_method(self, method):
        if self._is_async_server():

            def _method(*args, **kwargs):
                if iscoroutinefunction(method):
                    return asyncio.get_running_loop().create_task(method(*args, **kwargs))
                else:
                    async def _wrapper():
                        return method(*args, **kwargs)
                    
                    return _wrapper()

        else:

            def _method(*args, **kwargs):
                return method(*args, **kwargs)

        return _method

    def _is_render_request(self):
        request = _request()
        return request.id is not None


class BaseAsyncMiddleware(BaseMiddleware):
    server: AsyncServer

    def _is_async_server(self) -> bool:
        return True

    async def _emit(self, *args, **kwargs):
        return await self.server.emit(*args, **kwargs)

    def _make_handler(self, handler):
        async def _handler(sid, *data):
            result = handler(sid, *data)
            if result is None:
                return

            response_event, *response_data = result
            await self._emit(response_event, *response_data, to=sid)

        return _handler

    def on(self, event, handler):
        @wraps(handler)
        async def wrapper(sid, *args, **kwargs):
            try:
                WSRequest.make(sid)
                return await handler(sid, *args, **kwargs)
            except Exception as e:
                await self.server.emit("error", str(e), to=sid)
                raise e

        self.server.on(event, wrapper)
