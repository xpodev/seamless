from jsx.html import Div
from jsx.renderer import render

from tests.nested import App

def test_div():
    return Div(
        Div("Hello, World!", id="my-div"),
        Div(
            Div("Hello, World!", id="my-div"),
            Div("Hello, World!", id="my-div"),
            id="my-div",
            class_name="my-class",
        ),
    )


def test_app():
    return App()

# print(render(test_div()))
print(render(test_div(), prettify=True))
print()
print(render(test_app(), prettify=True))