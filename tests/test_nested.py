from .components import App, Page
from .base import TestCase


class NestedComponentsTest(TestCase):
    def test_nested_components(self):
        self.assertRender(App(), file="html/nested_components.html")

    def test_page_inheritance(self):
        self.maxDiff = None
        self.assertRender(Page(App()), file="html/page_inheritance.html")
