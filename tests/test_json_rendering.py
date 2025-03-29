from typing import Union, overload
from pydom import Component, Div
from pydom.element import Element
from pydom.types.rendering import Primitive, Renderable

from .base import TestCase


class TestRender(TestCase):
    @overload
    def assertRenderJson(
        self, component: Union[Renderable, Primitive], expected: dict, /, **kwargs
    ): ...
    @overload
    def assertRenderJson(
        self, component: Union[Renderable, Primitive], *, file: str, **kwargs
    ): ...

    def assertRenderJson(
        self,
        component: Union[Renderable, Primitive],
        expected=None,
        *,
        file=None,
        **kwargs,
    ):
        if expected is not None:
            self.assertRender(component, expected, to="json", **kwargs)
        elif file is not None:
            self.assertRender(component, file=file, to="json", **kwargs)
        else:
            raise ValueError("Expected or file must be provided")

    def test_render_json(self):
        self.assertRenderJson(Div(), {"type": "div", "children": [], "props": {}})

    def test_render_json_component(self):
        class MyComponent(Component):
            def render(self):
                return Div()

        self.assertRender(
            MyComponent(),
            {"type": "div", "children": [], "props": {}},
            to="json",
        )

    def test_render_json_element(self):
        class MyElement(Element):
            tag_name = "my-element"

        self.assertRenderJson(
            MyElement(),
            {"type": "my-element", "children": [], "props": {}},
        )

    def test_render_json_nested(self):
        self.assertRenderJson(
            Div(Div()),
            {
                "type": "div",
                "children": [{"type": "div", "children": [], "props": {}}],
                "props": {},
            },
        )

    def test_render_json_text(self):
        self.assertRenderJson(
            Div("Hello"),
            {"type": "div", "children": ["Hello"], "props": {}},
        )

    def test_render_json_attributes(self):
        self.assertRenderJson(
            Div(id="my-id"),
            {"type": "div", "children": [], "props": {"id": "my-id"}},
        )

    def test_render_json_nested_component(self):
        class MyComponent(Component):
            def render(self):
                return Div(
                    "Hello",
                    Div(),
                    id="my-id",
                    classes="my-class",
                )

        class MyComponent2(Component):
            def render(self):
                return Div(
                    MyComponent(),
                    classes="my-class",
                )

        self.assertRenderJson(
            MyComponent2(),
            {
                "type": "div",
                "children": [
                    {
                        "type": "div",
                        "children": [
                            "Hello",
                            {"type": "div", "children": [], "props": {}},
                        ],
                        "props": {"id": "my-id", "class": "my-class"},
                    }
                ],
                "props": {"class": "my-class"},
            },
        )

    def test_render_list_children(self):
        self.assertRenderJson(
            Div([Div(), Div()]),
            {
                "type": "div",
                "children": [
                    {"type": "div", "children": [], "props": {}},
                    {"type": "div", "children": [], "props": {}},
                ],
                "props": {},
            },
        )

    def test_render_nested_list_comprehension_children(self):
        self.assertRenderJson(
            Div([Div(i) for i in range(5)]),
            {
                "type": "div",
                "children": [
                    {"type": "div", "children": [str(i)], "props": {}} for i in range(5)
                ],
                "props": {},
            },
        )

    def test_render_nested_list_children(self):
        self.assertRenderJson(
            Div([Div([Div(), Div()]), Div([Div(), Div()])]),
            {
                "type": "div",
                "children": [
                    {
                        "type": "div",
                        "children": [
                            {"type": "div", "children": [], "props": {}},
                            {"type": "div", "children": [], "props": {}},
                        ],
                        "props": {},
                    },
                    {
                        "type": "div",
                        "children": [
                            {"type": "div", "children": [], "props": {}},
                            {"type": "div", "children": [], "props": {}},
                        ],
                        "props": {},
                    },
                ],
                "props": {},
            },
        )

    def test_render_list_as_component_children(self):
        class ItemList(Component):
            def __init__(self, items) -> None:
                self.items = items

            def render(self):
                return Div([Item(item=item) for item in self.items])

        class Item(Component):
            def __init__(self, item) -> None:
                self.item = item

            def render(self):
                return Div(self.item)

        self.assertRenderJson(
            ItemList(items=[f"item{i}" for i in range(1, 5)]),
            {
                "type": "div",
                "children": [
                    {"type": "div", "children": [f"item{i}"], "props": {}}
                    for i in range(1, 5)
                ],
                "props": {},
            },
        )