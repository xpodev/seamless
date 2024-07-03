from seamless import Element, Component, Div, render
from seamless.rendering.json import to_dict

import unittest


class TestRender(unittest.TestCase):
    def test_render(self):
        self.assertEqual(render(Div()), "<div></div>")

    def test_render_component(self):
        class MyComponent(Component):
            def render(self):
                return Div()

        self.assertEqual(render(MyComponent()), "<div></div>")

    def test_render_element(self):
        class MyElement(Element):
            tag_name = "my-element"

        self.assertEqual(render(MyElement()), "<my-element></my-element>")

    def test_render_nested(self):
        self.assertEqual(render(Div(Div())), "<div><div></div></div>")

    def test_render_text(self):
        self.assertEqual(render(Div("Hello")), "<div>Hello</div>")

    def test_render_attributes(self):
        self.assertEqual(render(Div(id="my-id")), '<div id="my-id"></div>')

    def test_render_children(self):
        self.assertEqual(render(Div(Div(), Div())), "<div><div></div><div></div></div>")

    def test_render_component_children(self):
        class MyComponent(Component):
            def render(self):
                return Div(Div(), Div())

        self.assertEqual(render(MyComponent()), "<div><div></div><div></div></div>")

    def test_render_element_children(self):
        class MyElement(Element):
            tag_name = "my-element"

        self.assertEqual(
            render(MyElement(Div(), Div())),
            "<my-element><div></div><div></div></my-element>",
        )

    def test_render_text_children(self):
        self.assertEqual(render(Div("Hello", "World")), "<div>HelloWorld</div>")

    def test_render_nested_children(self):
        self.assertEqual(
            render(Div(Div(Div()), Div(Div()))),
            "<div><div><div></div></div><div><div></div></div></div>",
        )

    def test_render_nested_text_children(self):
        self.assertEqual(
            render(Div(Div("Hello"), Div("World"))),
            "<div><div>Hello</div><div>World</div></div>",
        )

    def test_render_nested_mixed_children(self):
        self.assertEqual(
            render(Div(Div("Hello", id="my-div"), Div(), "World")),
            '<div><div id="my-div">Hello</div><div></div>World</div>',
        )

    def test_render_json(self):
        self.assertEqual(
            to_dict(Div()), {"type": "div", "children": [], "props": {}}
        )

    def test_render_json_component(self):
        class MyComponent(Component):
            def render(self):
                return Div()

        self.assertEqual(
            to_dict(MyComponent()), {"type": "div", "children": [], "props": {}}
        )

    def test_render_json_element(self):
        class MyElement(Element):
            tag_name = "my-element"

        self.assertEqual(
            to_dict(MyElement()),
            {"type": "my-element", "children": [], "props": {}},
        )

    def test_render_json_nested(self):
        self.assertEqual(
            to_dict(Div(Div())),
            {
                "type": "div",
                "children": [{"type": "div", "children": [], "props": {}}],
                "props": {},
            },
        )

    def test_render_json_text(self):
        self.assertEqual(
            to_dict(Div("Hello")),
            {"type": "div", "children": ["Hello"], "props": {}},
        )

    def test_render_json_attributes(self):
        self.assertEqual(
            to_dict(Div(id="my-id")),
            {"type": "div", "children": [], "props": {"id": "my-id"}},
        )

    def test_render_json_nested_component(self):
        class MyComponent(Component):
            def render(self):
                return Div(
                    "Hello",
                    Div(),
                    id="my-id",
                    class_name="my-class",
                )
            
        class MyComponent2(Component):
            def render(self):
                return Div(
                    MyComponent(),
                    class_name="my-class",
                )

        self.assertEqual(
            to_dict(MyComponent2()),
            {
                "type": "div",
                "children": [
                    {
                        "type": "div",
                        "children": ["Hello", {"type": "div", "children": [], "props": {}}],
                        "props": {"id": "my-id", "class": "my-class"},
                    }
                ],
                "props": {"class": "my-class"},
            }
        )
