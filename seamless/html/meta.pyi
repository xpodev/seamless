from typing import Literal, overload
from pydom.element import Element

from ..types import ChildType

HttpEquivOptions = Literal[
    "content-security-policy",
    "content-type",
    "default-style",
    "x-ua-compatible",
    "refresh",
]


class Meta(Element):

    @overload
    def __init__(
        self, *children: ChildType, http_equiv: HttpEquivOptions, content: str
    ): ...
    @overload
    def __init__(self, *children: ChildType, name: str, content: str): ...
    @overload
    def __init__(self, *children: ChildType, charset: str): ...
    @overload
    def __init__(self, *children: ChildType, itemprop: str): ...

    def __init__(self, *children: ChildType, **kwargs): ...
