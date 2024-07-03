import unittest
from seamless import render
from .components import App, Page


class NestedComponentsTest(unittest.TestCase):
    def test_nested_components(self):
        self.assertEqual(
            render(App()),
            '<div class="card"><h3 class="card-title">Card title</h3><hr><div>Card content</div></div>',
        )

    def test_page_inheritance(self):
        self.maxDiff = None
        self.assertEqual(
            render(Page(App())),
            '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title></title><link rel="stylesheet" href="/static/style.css"></head><body dir="ltr"><div class="card"><h3 class="card-title">Card title</h3><hr><div>Card content</div></div></body></html>',
        )
