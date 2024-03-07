from functools import wraps
from mimetypes import guess_type
from pathlib import Path

from socketio.base_server import BaseServer
from socketio import AsyncServer

from ..server.database import DB
from ..server.ws_router import ws_router
from ..server.request import set_request, WSRequest


class BaseMiddleware:
    STATIC_FOLDER = Path(__file__).parent.parent / "server/static"

    def __init__(self, app, socket_path="/socket.io"):
        self.socket_path = f"/{socket_path.strip('/')}"
        self.server = self._server_class()(cors_allowed_origins=[])
        self.app = self._app_class()(self.server, app, socketio_path=socket_path)
        self._setup()

    def _setup(self):
        self._setup_events()

    def _emit(self, *args, **kwargs):
        return self.server.emit(*args, **kwargs)

    def _setup_events(self):
        self.on("disconnect", self._handle_disconnect)
        self.on("dom_event", self.dom_event)

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
        component_id = component_id
        try:
            DB.invoke_element_event(component_id, event, event_data)
        except KeyError:
            raise Exception(
                f"Element {component_id} not found. Did you forget to claim your http rendered components?"
            )

    def _handle_disconnect(self, sid: str):
        DB.release_elements(sid)

    def on(self, event, handler):
        @wraps(handler)
        def wrapper(sid, *args, **kwargs):
            try:
                set_request(WSRequest(sid))
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
                set_request(WSRequest(sid))
                return await handler(sid, *args, **kwargs)
            except Exception as e:
                await self.server.emit("error", str(e), to=sid)

        self.server.on(event, wrapper)
