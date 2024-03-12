from functools import wraps
from inspect import iscoroutinefunction
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import Response
from jsx import *
from jsx.middlewares import ASGIMiddleware
from jsx.styling import CSS
from .server.common import Page

CSS.set_root_folder(Path(__file__).parent / "server/static")
app = FastAPI()


app.add_middleware(
    ASGIMiddleware,
)


def _make_response(response):
    if isinstance(response, (Component, Element)):
        if not isinstance(response, Page):
            response = Page(response)

        response = Response(render(response), media_type="text/html")

    return response


@wraps(app.get)
def get(path: str, **kwargs):
    def wrapper(_handler):
        if iscoroutinefunction(_handler):

            @wraps(_handler)
            async def handler(*args, **kwargs):
                response = await _handler(*args, **kwargs)
                return _make_response(response)

        else:

            @wraps(_handler)
            def handler(*args, **kwargs):
                response = _handler(*args, **kwargs)
                return _make_response(response)

        app.get(path, **kwargs)(handler)

    return wrapper


def card():
    styles = CSS.module("card.css")
    return Div("Hello, world!", class_name=styles.card)


@get("/")
async def index():
    return card()


@app.get("/static/main.css")
def css_file():
    return Response(CSS.export(), media_type="text/css")


@app.get("/static/main.min.css")
def css_file():
    return Response(CSS.export(minified=True), media_type="text/css")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
