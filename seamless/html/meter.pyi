from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLMeterElement
from ..types import ChildType


class Meter(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLMeterElement]): ...
