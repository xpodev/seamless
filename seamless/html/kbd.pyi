from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLElementProps
from ..types import ChildType


class Kbd(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLElementProps]): ...
