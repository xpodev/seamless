from functools import wraps
from inspect import iscoroutinefunction
from pathlib import Path
from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from seamless import *
from seamless.middlewares.asgi import ASGIMiddleware
from seamless.styling import CSS
from .server.common import Card, Page, SuperCard, SampleComponent

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


def click_handler(*args, **kwargs):
    print("Button clicked")


def card():
    return SampleComponent("world")


@get("/")
def index():
    return card()


@app.get("/static/main.js")
def socket_io_static():
    return FileResponse(Path(__file__).parent / "server/static/main.js")


@app.get("/static/main.css")
def css_file():
    return Response(CSS.to_css_string(), media_type="text/css")


@app.get("/static/main.min.css")
def css_file_min():
    return Response(CSS.to_css_string(minified=True), media_type="text/css")
