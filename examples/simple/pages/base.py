from seamless import Link, Script, Style
from seamless.components import Page
from seamless.styling import CSS

class BasePage(Page):
    def head(self):
        yield from super().head()
        yield Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
        )
        yield Script(src="https://cdn.jsdelivr.net/npm/@python-seamless/core@0.8.6/umd/seamless.init.js", defer=True)
        yield Style(
            "html, body { height: 100%; }" +
            CSS.to_css_string(minified=True)
        )
