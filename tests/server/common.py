from jsx.html import *
from jsx import Component, ContainerComponent
from jsx.renderer import render
from jsx.server.request import request
from jsx.server.database import DB

def index():
    return render(Page(SampleComponent(name="world")))


def db_memory():
    return {
        "elements": len(DB.elements),
        "ids": len(DB.element_ids),
        "unclaimed": list(DB._all_unclaimed.keys())
    }


class Page(ContainerComponent):
    def render(self):
        return Fragment(
            "<!DOCTYPE html>",
            Html(
                Head(
                    Title("JSX"),
                    Meta(name="jsx-claim-id", value=request().id),
                    Script(src="/socket.io/static/main.js"),
                ),
                Body(
                    Div(
                        Div(
                            f"JSX Claim ID: {request().id}"
                        ),
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
