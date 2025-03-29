from pydom import Div, Script, Style

from .base import TestCase


class EscapingComponentsTest(TestCase):
    def test_escaping(self):
        self.assertRender(
            Div(
                "<script>"
                "console.log('hello world');"
                "if (a < 2) {"
                "   console.log('a is less than 2');"
                "}"
                "</script>"
            ),
            "<div>"
            "&lt;script&gt;"
            "console.log(&#x27;hello world&#x27;);"
            "if (a &lt; 2) {"
            "   console.log(&#x27;a is less than 2&#x27;);"
            "}"
            "&lt;/script&gt;"
            "</div>",
        )

    def test_escaping_style(self):
        self.assertRender(
            Style("body { color: red; }"),
            "<style>body { color: red; }</style>",
        )

    def test_escaping_script(self):
        self.assertRender(
            Script(
                "console.log('hello world'); if (a < 2) { console.log('a is less than 2'); }"
            ),
            file="html/escaping_script.html",
        )
