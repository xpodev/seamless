from seamless import Link, Script
from seamless.components import Page


class BasePage(Page):
    def head(self):
        yield from super().head()
        yield Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
        )
        yield Script(src="/static/main.js", defer=True)
