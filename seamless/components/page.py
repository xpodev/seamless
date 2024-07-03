from typing import Literal, TypedDict
from .base import Component
from ..html import (
    Fragment,
    Html,
    Head,
    Title,
    Body,
    Meta,
)


class _HtmlProps(TypedDict):
    lang: str


class _HeadProps(TypedDict): ...


class _BodyProps(TypedDict):
    dir: Literal["ltr", "rtl"]


class Page(Component, name="SeamlessBasePage"):
    def __init__(
        self,
        *,
        title=None,
        html_props: _HtmlProps = None,
        head_props: _HeadProps = None,
        body_props: _BodyProps = None,
    ):
        self.title = title
        self._html_props = html_props or {"lang": "en"}
        self._head_props = head_props or {}
        self._body_props = body_props or {"dir": "ltr"}

    def head(self):
        """
        The children that will be inside the `head` tag.
        """
        return (
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Title(self.title),
        )

    def body(self):
        """
        The children that will be inside the `body` tag.
        """
        return self.children

    def render(self):
        return Fragment(
            "<!DOCTYPE html>",
            Html(**self._html_props)(
                Head(**self._head_props)(*self.head()),
                Body(**self._body_props)(*self.body()),
            ),
        )

    def __init_subclass__(cls, title: str = None, **kwargs) -> None:
        super().__init_subclass__(**kwargs)

        if title is None:
            return

        original_init = cls.__init__

        def __init__(self, *args, **kwargs):
            kwargs["title"] = kwargs.get("title", title)
            original_init(self, *args, **kwargs)

        cls.__init__ = __init__
