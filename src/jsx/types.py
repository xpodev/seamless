from typing import TypeAlias, TYPE_CHECKING

if TYPE_CHECKING:
    from . import Component, Element


Primitive: TypeAlias = "str | int | float | bool | None" 
Renderable: TypeAlias = "Component | Element"
RenderResult: TypeAlias = "Renderable | Primitive"

ChildrenType: TypeAlias = "Renderable | list[Renderable] | Primitive | list[Primitive]"
