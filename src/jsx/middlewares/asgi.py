from functools import partial
from socketio import AsyncServer, ASGIApp

from .base import BaseAsyncMiddleware
from ..server.request import set_request, HTTPRequest, request


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
        if scope["type"] == "http":
            set_request(HTTPRequest())
            if (
                scope["path"].startswith(f"{self.socket_path}/static/")
                and scope["method"] == "GET"
            ):
                return await self.static_handler(scope, receive, send)

            async def c(message):
                headers = [[b"Set-Cookie", f"_jsx_claimId={request().id}".encode()]]
                if "headers" not in message:
                    message["headers"] = []

                message["headers"].extend(headers)
                await send(message)

            return await self.app(scope, receive, c)

        await self.app(scope, receive, send)

    def _app_class(self):
        return ASGIApp

    def _server_class(self):
        return partial(AsyncServer, async_mode="asgi")
