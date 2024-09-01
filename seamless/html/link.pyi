from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLLinkElement
from ..types import ChildType


class Link(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLLinkElement]): ...
