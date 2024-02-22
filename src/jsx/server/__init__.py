from functools import wraps
from pathlib import Path
from socketio import AsyncServer, ASGIApp
from .database import ElementsDatabase
from .ws_router import ws_router

db = ElementsDatabase()


class JSXServer:
    def __init__(self, **config):
        self.app = None
        config["async_mode"] = "asgi"
        self.server = AsyncServer(**config)
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

    def mount(self, app, socket_path="/socket.io"):
        app.mount(socket_path, ASGIApp(self.server))

    def scripts_path(self):
        return Path(__file__).parent / "scripts"

    async def dom_event(self, sid, data, event_data):
        component_id, event = data.split(":")
        component_id = component_id
        db.invoke_component_event(component_id, event, event_data)

    def on(self, event, handler):
        @wraps(handler)
        async def wrapper(sid, *args, **kwargs):
            try:
                return await handler(sid, *args, **kwargs)
            except Exception as e:
                await self.server.emit("error", str(e), to=sid)

        self.server.on(event, wrapper)
