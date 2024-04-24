from typing import Literal, TypedDict
from .base import (
    ContainerComponent,
)
from ..html import (
    Fragment,
    Html,
    Head,
    Title,
    Body,
    Meta,
)


class _HeadProps(TypedDict):
    lang: str


class _BodyProps(TypedDict):
    dir: Literal["ltr", "rtl"]


class Page(ContainerComponent):
    def __init__(
        self,
        title=None,
        *,
        head_props: _HeadProps = None,
        body_props: _BodyProps = None,
    ):
        self.title = title
        self._head_props = head_props or {"lang": "en"}
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
            Html(
                Head(**self._head_props)(*self.head()),
                Body(**self._body_props)(*self.body()),
            ),
        )
