from typing import Collection, TypeAlias, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from seamless import Component
    from seamless.element import Element


Primitive: TypeAlias = str | int | float | bool | None
Renderable: TypeAlias = Union["Element", "Component"]

ChildrenType: TypeAlias = (
    Renderable | Collection[Renderable] | Primitive | Collection[Primitive]
)
RenderResult: TypeAlias = Renderable | Primitive
