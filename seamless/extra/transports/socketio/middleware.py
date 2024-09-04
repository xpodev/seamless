from typing import Optional
from socketio import ASGIApp

from pydom.context import Context, get_context

from .transport import SocketIOTransport


class SocketIOMiddleware:
    def __init__(
        self, app, socket_path="/socket.io", context: Optional[Context] = None
    ):
        context = get_context(context)
        self.socket_path = f"/{socket_path.strip('/')}"
        try:
            transport = context.get_feature(SocketIOTransport)
        except KeyError:
            raise ValueError(
                "SocketIOTransport feature is required when using SocketIOMiddleware. "
                "Please add it to the context."
            )

        self.app = ASGIApp(transport.server, app, socketio_path=self.socket_path)

    async def __call__(self, scope, receive, send):
        await self.app(scope, receive, send)
