from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from jsx import Component, ContainerComponent
from jsx.middlewares import ASGIMiddleware
from jsx.html import *
from jsx.renderer import render

HERE = Path(__file__).parent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    ASGIMiddleware,
)

@app.get("/c", response_class=HTMLResponse)
def index():
    return render(Page(SampleComponent(name="world")))


class Page(ContainerComponent):
    def render(self):
        return Fragment(
            "<!DOCTYPE html>",
            Html(
                Head(
                    Title("JSX"),
                    Script(src="/socket.io/static/main.js"),
                ),
                Body(
                    Div(
                        *self.children,
                        id="root",
                    )
                ),
            ),
        )
    


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
            Button("Click me", on_click=self.click),
            AnotherComponent(name="world"),
        )
    
    def click(self, event):
        print("clicked", event)
