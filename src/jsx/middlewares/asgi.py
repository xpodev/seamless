from functools import partial
from socketio import AsyncServer, ASGIApp

from .base import BaseAsyncMiddleware


class ASGIMiddleware(BaseAsyncMiddleware):
    async def __call__(self, scope, receive, send):
        await self.app(scope, receive, send)

    def _app_class(self):
        return ASGIApp

    def _server_class(self):
        return partial(AsyncServer, async_mode="asgi")
