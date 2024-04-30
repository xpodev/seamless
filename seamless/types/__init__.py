from typing import Collection, TypeAlias, TYPE_CHECKING

if TYPE_CHECKING:
    from seamless import Element, Component


Primitive: TypeAlias = str | int | float | bool | None
Renderable: TypeAlias = "Element" | "Component"

ChildrenType: TypeAlias = (
    Renderable | Collection[Renderable] | Primitive | Collection[Primitive]
)
RenderResult: TypeAlias = Renderable | Primitive
