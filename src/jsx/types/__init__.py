from typing import Protocol, Collection, TypeAlias

Primitive: TypeAlias = str | int | float | bool | None


class Renderable(Protocol):
    def render(self) -> "RenderResult": ...


ChildrenType: TypeAlias = Renderable | Collection[Renderable] | Primitive | Collection[Primitive]
RenderResult: TypeAlias = Renderable | Primitive

