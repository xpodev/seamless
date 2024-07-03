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

    def __init_subclass__(cls, title=None, **kwargs) -> None:
        super().__init_subclass__(**kwargs)

        if title is None:
            return

        original_init  = cls.__init__
        def __init__(self, *args, **kwargs):
            kwargs["title"] = kwargs.get("title", title)
            original_init(self, *args, **kwargs)

        cls.__init__ = __init__
