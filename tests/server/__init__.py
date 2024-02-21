from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from jsx.server import JSXServer
from jsx import Component
from jsx.html import *

HERE = Path(__file__).parent

app = FastAPI()
jsx_server = JSXServer(cors_allowed_origins="*")
app.mount("/_jsx/scripts", StaticFiles(directory=jsx_server.scripts_path()), name="scripts")
jsx_server.mount(app, socket_path="/socket.io")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return FileResponse(HERE / "static/index.html")


class AnotherComponent(Component):
    def __init__(self, name):
        self.name = name

    def render(self):
        return Div(
            Div(
                H2("Another component"),
                P(f"Hello, {self.name}!"),
            )
        )
    

class SampleComponent(Component):
    def __init__(self, name):
        self.name = name

    def render(self):
        return Div(
            H1(f"Hello, {self.name}!"),
            P("This is a JSX component"),
            AnotherComponent(name="world"),
        )
