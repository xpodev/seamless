from socketio import AsyncServer
from functools import wraps

from ..server.database import ElementsDatabase
from ..server.ws_router import ws_router

db = ElementsDatabase()


class BaseMiddleware:
    server: AsyncServer

    def __init__(self, app, socket_path="/socket.io"):
        self.server = self._server_class()(cors_allowed_origins=[])
        self.app = self._app_class()(self.server, app, socketio_path=socket_path)
        self._setup()

    def _setup(self):
        self._setup_events()

    def _setup_events(self):
        self.on("dom_event", self.dom_event)

        for command, handler in ws_router.items():
            self.on(command, self._make_handler(handler))

    def _make_handler(self, handler):
        async def _handler(sid, *data):
            response_event, *response_data = handler(*data)
            await self.server.emit(response_event, *response_data, to=sid)

        return _handler

    async def dom_event(self, sid, data: str, event_data):
        component_id, event = data.split(":")
        component_id = component_id
        db.invoke_component_event(component_id, event, event_data)

    def on(self, event, handler):
        @wraps(handler)
        async def wrapper(sid, *args, **kwargs):
            try:
                return await handler(sid, *args, **kwargs)
            except Exception as e:
                print(e)
                await self.server.emit("error", str(e), to=sid)

        self.server.on(event, wrapper)

    def _app_class(self):
        raise NotImplementedError("self._app_class is not implemented")

    def _server_class(self):
        raise NotImplementedError("self._server_class is not implemented")
