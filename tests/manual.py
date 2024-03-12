from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response
from starlette.middleware.base import BaseHTTPMiddleware
from jsx import *
from jsx.middlewares import ASGIMiddleware
from jsx.styling import CSS
from .server.common import Page

CSS.set_root_folder(Path(__file__).parent / "server/static")
app = FastAPI()

class JSXMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        if not hasattr(response, "body"):
            return response

        body = response.body
        if isinstance(body, Component):
            if not isinstance(body, Page):
                body = Page(body)
            body = render(body)
            response = Response(body, media_type="text/html")

        return response


app.add_middleware(
    ASGIMiddleware,
)
app.add_middleware(
    JSXMiddleware,
)


def card():
    styles = CSS.module("card.css")
    return Div("Hello, world!", class_name=styles.card)


@app.get("/")
async def index():
    return card()


@app.get("/static/main.css")
def css_file():
    return Response(CSS.output(minified=True), media_type="text/css")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
