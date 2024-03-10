from functools import partial
from socketio import AsyncServer, ASGIApp

from .base import BaseAsyncMiddleware
from ..server.request import set_request, HTTPRequest


class ASGIMiddleware(BaseAsyncMiddleware):
    async def static_handler(self, scope, receive, send):
        http_path: str = scope["path"]
        replace_path = f"{self.socket_path}/static/"
        file_path = self.STATIC_FOLDER / http_path.removeprefix(replace_path)
        if not file_path.exists():
            await send(
                {
                    "type": "http.response.start",
                    "status": 404,
                    "headers": [(b"content-type", b"text/plain")],
                }
            )
            await send({"type": "http.response.body", "body": b"Not Found"})
            return

        mime_type = self._mime_type(file_path.name)
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [(b"content-type", mime_type.encode())],
            }
        )
        with file_path.open("rb") as file:
            await send({"type": "http.response.body", "body": file.read()})

    async def __call__(self, scope, receive, send):
        async def _send(message):
            await send(message)

        if scope["type"] == "http":
            request = HTTPRequest.make(scope, type="asgi")
            if (
                request.path.startswith(f"{self.socket_path}/static/")
                and request.method == "GET"
            ):
                return await self.static_handler(scope, receive, send)

            if self._is_render_request():

                async def _send(message):
                    if "headers" not in message:
                        message["headers"] = []

                    message["headers"].extend(
                        self._make_cookie_header("_jsx_claimId", request.id)
                    )
                    await send(message)

            elif request.path.startswith(self.socket_path):
                if "_jsx_claimId" in request.cookies:

                    async def _send(message):
                        if "headers" not in message:
                            message["headers"] = []

                        message["headers"].extend(self._remove_cookie("_jsx_claimId"))

                        await send(message)

        await self.app(scope, receive, _send)

    def _app_class(self):
        return ASGIApp

    def _server_class(self):
        return partial(AsyncServer, async_mode="asgi")
