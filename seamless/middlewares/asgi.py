from functools import partial
from socketio import AsyncServer, ASGIApp

from .base import BaseAsyncMiddleware, CLAIM_COOKIE_NAME
from ..context.request import HTTPRequest


class ASGIMiddleware(BaseAsyncMiddleware):
    async def __call__(self, scope, receive, send):
        async def _send(message):
            await send(message)

        if scope["type"] == "http":
            request = HTTPRequest.make(scope, type="asgi")

            async def _send(message):
                if message["type"] != "http.response.start":
                    return await send(message)

                if self._is_render_request():
                    if "headers" not in message:
                        message["headers"] = []

                    message["headers"].append(
                        self._make_cookie_header(CLAIM_COOKIE_NAME, request.id)
                    )

                elif request.path.startswith(self.socket_path):
                    if CLAIM_COOKIE_NAME in request.cookies:
                        if "headers" not in message:
                            message["headers"] = []

                        message["headers"].append(
                            self._remove_cookie(CLAIM_COOKIE_NAME)
                        )

                await send(message)

        await self.app(scope, receive, _send)

    def _app_class(self):
        return ASGIApp

    def _server_class(self):
        return partial(AsyncServer, async_mode="asgi")
