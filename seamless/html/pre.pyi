from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLPreElement
from ..types import ChildType


class Pre(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLPreElement]): ...
