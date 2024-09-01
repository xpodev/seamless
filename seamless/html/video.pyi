from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLVideoElement
from ..types import ChildType


class Video(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLVideoElement]): ...
