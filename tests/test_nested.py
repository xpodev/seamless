import unittest
from jsx.renderer import render
from .components import App


class NestedComponentsTest(unittest.TestCase):
    def test_nested_components(self):
        self.assertEqual(
            render(App()),
            '<div class="card"><h3 class="card-title">Card title</h3><hr><div>Card content</div></div>',
        )