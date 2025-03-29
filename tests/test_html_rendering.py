from pydom import Component, Div, render
from pydom.element import Element
from pydom.errors import RenderError

from .base import TestCase


class TestRender(TestCase):
    def test_render(self):
        self.assertRender(Div(), "<div></div>")

    def test_render_component(self):
        class MyComponent(Component):
            def render(self):
                return Div()

        self.assertRender(MyComponent(), "<div></div>")

    def test_render_element(self):
        class MyElement(Element):
            tag_name = "my-element"

        self.assertRender(MyElement(), "<my-element></my-element>")

    def test_render_inline_element(self):
        class MyInlineElement(Element):
            tag_name = "my-element"
            inline = True

        self.assertRender(MyInlineElement(), "<my-element />")

    def test_render_nested(self):
        self.assertRender(Div(Div()), "<div><div></div></div>")

    def test_render_text(self):
        self.assertRender(Div("Hello"), "<div>Hello</div>")

    def test_render_attributes(self):
        self.assertRender(Div(id="my-id"), '<div id="my-id"></div>')

    def test_render_children(self):
        self.assertRender(Div(Div(), Div()), "<div><div></div><div></div></div>")

    def test_render_component_children(self):
        class MyComponent(Component):
            def render(self):
                return Div(Div(), Div())

        self.assertRender(MyComponent(), "<div><div></div><div></div></div>")

    def test_render_element_children(self):
        class MyElement(Element):
            tag_name = "my-element"

        self.assertRender(
            MyElement(Div(), Div()),
            "<my-element><div></div><div></div></my-element>",
        )

    def test_render_text_children(self):
        self.assertRender(Div("Hello", "World"), "<div>HelloWorld</div>")

    def test_render_nested_children(self):
        self.assertRender(
            Div(Div(Div()), Div(Div())),
            "<div><div><div></div></div><div><div></div></div></div>",
        )

    def test_render_nested_text_children(self):
        self.assertRender(
            Div(Div("Hello"), Div("World")),
            "<div><div>Hello</div><div>World</div></div>",
        )

    def test_render_nested_mixed_children(self):
        self.assertRender(
            Div(Div("Hello", id="my-div"), Div(), "World"),
            '<div><div id="my-div">Hello</div><div></div>World</div>',
        )

    def test_render_list_children(self):
        self.assertRender(Div([Div(), Div()]), "<div><div></div><div></div></div>")

    def test_render_nested_list_comprehension_children(self):
        self.assertRender(
            Div([Div(i) for i in range(5)]),
            "<div><div>0</div><div>1</div><div>2</div><div>3</div><div>4</div></div>",
        )

    def test_render_nested_list_children(self):
        self.assertRender(
            Div([Div([Div()]), Div([Div()])]),
            "<div><div><div></div></div><div><div></div></div></div>",
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

        self.assertRender(
            ItemList(items=[f"item{i}" for i in range(1, 5)]),
            "<div><div>item1</div><div>item2</div><div>item3</div><div>item4</div></div>",
        )

    def test_render_invalid_children(self):
        with self.assertRaises(RenderError):
            render(Div(object()))  # type: ignore - this is intentional
