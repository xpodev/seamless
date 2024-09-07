from typing import Optional, overload, Iterable

from pydom import Component
from pydom.utils.functions import to_iter

from ..html import (
    Fragment,
    Html,
    Head,
    Title,
    Body,
    Meta,
)

from ..types import ChildType, ChildrenType
from ..types.html import HTMLHtmlElement, HTMLBodyElement, HTMLHeadElement


class Page(Component):
    @overload
    def __init__(
        self,
        *children: ChildType,
        title: Optional[str] = None,
        html_props: Optional[HTMLHtmlElement] = None,
        head_props: Optional[HTMLHeadElement] = None,
        body_props: Optional[HTMLBodyElement] = None,
    ): ...
    @overload
    def __init__(
        self,
        *,
        children: ChildrenType,
        title: Optional[str] = None,
        html_props: Optional[HTMLHtmlElement] = None,
        head_props: Optional[HTMLHeadElement] = None,
        body_props: Optional[HTMLBodyElement] = None,
    ): ...

    def __init__(  # type: ignore
        self,
        *,
        title: Optional[str] = None,
        html_props: Optional[HTMLHtmlElement] = None,
        head_props: Optional[HTMLHeadElement] = None,
        body_props: Optional[HTMLBodyElement] = None,
    ):
        self.title = title
        self._html_props = html_props or {"lang": "en"}
        self._head_props = head_props or {}
        self._body_props = body_props or {"dir": "ltr"}

    def head(self) -> Iterable["ChildType"]:
        """
        The children that will be inside the `head` tag.
        """
        return (
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Title(self.title) if self.title else None,
        )

    def body(self) -> Iterable[ChildType]:
        """
        The children that will be inside the `body` tag.
        """
        return self.children

    def render(self):
        return Fragment(
            "<!DOCTYPE html>",
            Html(**self._html_props)(
                Head(**self._head_props)(*to_iter(self.head())),
                Body(**self._body_props)(*to_iter(self.body())),
            ),
        )

    def __init_subclass__(cls, title: Optional[str] = None, **kwargs) -> None:
        super().__init_subclass__(**kwargs)

        if title is None:
            return

        original_init = cls.__init__

        def __init__(self, *args, **kwargs):
            kwargs["title"] = kwargs.get("title", title)
            original_init(self, *args, **kwargs)

        cls.__init__ = __init__

    __seamless_name__ = "SeamlessBasePage"
