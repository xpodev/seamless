from typing import Literal, overload
from ..types import ChildType
from ..element import Element


HttpEquivOptions = Literal["content-security-policy", "content-type", "default-style", "x-ua-compatible", "refresh"]


class Meta(Element):

    @overload
    def __init__(self, *children: ChildType, http_equiv: HttpEquivOptions, content: str): ...
    @overload
    def __init__(self, *children: ChildType, name: str, content: str): ...
    @overload
    def __init__(self, *children: ChildType, charset: str): ...
    @overload
    def __init__(self, *children: ChildType, itemprop: str): ...

    def __init__(self, *children: ChildType, **kwargs):
        super().__init__(*children, **kwargs)

    tag_name = "meta"
    inline = True
