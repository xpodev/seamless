from jsx.html import *
from jsx import Component, ContainerComponent, render
from jsx.styling import CSS
from jsx.server.database import DB
from jsx.types.events import MouseEvent


def index():
    return render(Page(SampleComponent(name="world")))


def css_file(minified=False):
    return CSS.to_css_string(minified)


def db_memory():
    return {
        "elements": len(DB.elements),
        "ids": len(DB.element_ids),
        "unclaimed": list(DB._all_unclaimed.keys()),
    }


class Page(ContainerComponent):
    def render(self):
        return Fragment(
            "<!DOCTYPE html>",
            Html(
                Head(
                    Title("JSX"),
                    Script(src="/static/main.js"),
                    Link(rel="stylesheet", href="/static/main.css"),
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

    def click(self, event: dict[str, str]):
        print("clicked", event)


class Card(ContainerComponent):
    def __init__(self, rounded=True) -> None:
        self.rounded = rounded

    def render(self):
        styles = CSS.module("card.css")
        return Div(
            class_name=styles.card,
            style={"border-radius": "5px"} if self.rounded else None,
        )(*self.children)


class SuperCard(Card):
    def __init__(self, rounded=True, is_super=False) -> None:
        self.rounded = rounded
        self.is_super = is_super

    def render(self):
        styles = CSS.module("card.css")
        return Div(
            class_name=styles.card,
            style={"border-radius": "10px"} if self.rounded else None,
        )(Div("Super card!" if self.is_super else "Card!"), *self.children)
