from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLScriptElement
from ..types import ChildType


class Script(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLScriptElement]): ...
