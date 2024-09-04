from functools import wraps
from inspect import iscoroutinefunction
from pathlib import Path
from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pydom.element import Element
from seamless import *
from seamless.extra.transports.socketio.middleware import SocketIOMiddleware
from seamless.styling import CSS
from seamless.components import Page as BasePage
from .server.common import Card, Page, SuperCard, SampleComponent
from .components import Page as TestPage, App

app = FastAPI()
app.add_middleware(SocketIOMiddleware)


def _make_response(response):
    if isinstance(response, (Component, Element)):
        if not isinstance(response, BasePage):
            response = BasePage(response)

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


def card(super=True):
    return (SuperCard(is_super=True) if super else Card())(
        SampleComponent(name="world"),
        Button("Click me"),
        Form(on_submit=submit, action="#")(
            Input(placeholder="Enter your name", name="name"),
            Button("Submit"),
        ),
    )


from typing import Generic, TypeVar

T = TypeVar("T")


class SubmitEvent(BaseModel, Generic[T]):
    type: str
    data: T


class MyForm(BaseModel):
    name: str


def submit(event: SubmitEvent[MyForm]):
    print(f"Form submitted: name = {event.data.name}")


@get("/")
def index(super: bool = True):
    return TestPage(App())


@app.get("/static/main.js")
def socket_io_static():
    return FileResponse(Path(__file__).parent / "server/static/main.js")


@app.get("/static/main.css")
def css_file():
    return Response(CSS.to_css_string(), media_type="text/css")


@app.get("/static/main.min.css")
def css_file_min():
    return Response(CSS.to_css_string(minified=True), media_type="text/css")
