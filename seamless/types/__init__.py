from typing import Collection, TypeAlias

from ..core import Component
from ..element import Element

Primitive: TypeAlias = str | int | float | bool | None
Renderable: TypeAlias = Element | Component

ChildType: TypeAlias = Renderable | Primitive
RenderResult: TypeAlias = Renderable | Primitive
ChildrenType: TypeAlias = Collection[ChildType]
