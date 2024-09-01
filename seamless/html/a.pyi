from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLAnchorElement
from ..types import ChildType


class A(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLAnchorElement]): ...
