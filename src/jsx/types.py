from typing import TypeAlias, Protocol


Primitive: TypeAlias = "str | int | float | bool | None"
RenderResult: TypeAlias = "Renderable | Primitive"

ChildrenType: TypeAlias = "Renderable | list[Renderable] | Primitive | list[Primitive]"

class Renderable(Protocol):
    def render(self) -> RenderResult: ...
