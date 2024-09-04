from json import dumps
from pathlib import Path
from urllib.parse import parse_qs

from pydom import Component, Context
from pydom.rendering.render_state import RenderState
from pydom.utils.functions import random_string
from socketio import AsyncServer

from ....core.javascript import JS
from ....core.empty import Empty
from ..client_id import ClientID
from ..errors import TransportConnectionRefused
from ..transport import TransportFeature

HERE = Path(__file__).parent


class SocketIOTransport(TransportFeature):
    def __init__(self, context: Context):
        super().__init__(context)

        self.server = AsyncServer(async_mode="asgi")

        self.server.on("connect", self.on_connect)
        self.server.on("*", self.on_event)
        self.server.on("disconnect", self.on_disconnect)

    async def on_connect(self, sid, env):
        try:
            query = parse_qs(env.get("QUERY_STRING", ""))
            client_id = query.get("client_id", [None])[0]
            await self.connect(client_id, env)
            await self.server.save_session(sid, {"client_id": client_id})
        except TransportConnectionRefused:
            await self.server.disconnect(sid)

    async def on_event(self, event_name, sid, *data):
        client_id = await self._client_id(sid)
        with self.context.injector.scope({ClientID: lambda: client_id}):
            res = await self.event(event_name, client_id, *data)
            return res

    async def on_disconnect(self, sid):
        client_id = await self._client_id(sid)
        await self.disconnect(client_id)

    async def _client_id(self, sid):
        session = await self.server.get_session(sid)
        return session["client_id"]

    @staticmethod
    def init(config=None):
        init_js = JS(file=HERE / "socketio.init.js", async_=True)

        class InitSocketIO(Component, inject_render=True):
            def render(self, render_state: RenderState):
                client_id = render_state.custom_data.setdefault(
                    "transports.client_id", random_string(24)
                )

                socket_options = config or {}
                socket_options.setdefault("query", {})["client_id"] = client_id

                return Empty(
                    init=JS(
                        f"""
                        const socketIOConfig = {dumps(socket_options)};
                        """
                    )
                    + init_js
                )

        return InitSocketIO()
