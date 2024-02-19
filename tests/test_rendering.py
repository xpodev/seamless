from jsx.html import Div
from jsx.renderer import render
from jsx import Element, Component

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

        self.assertEqual(render(MyElement(Div(), Div())), "<my-element><div></div><div></div></my-element>")

    def test_render_text_children(self):
        self.assertEqual(render(Div("Hello", "World")), "<div>HelloWorld</div>")

    def test_render_nested_children(self):
        self.assertEqual(render(Div(Div(Div()), Div(Div()))), "<div><div><div></div></div><div><div></div></div></div>")

    def test_render_nested_text_children(self):
        self.assertEqual(render(Div(Div("Hello"), Div("World"))), "<div><div>Hello</div><div>World</div></div>")

    def test_render_nested_mixed_children(self):
        self.assertEqual(render(Div(Div("Hello", id="my-div"), Div(), "World")), '<div><div id="my-div">Hello</div><div></div>World</div>')
