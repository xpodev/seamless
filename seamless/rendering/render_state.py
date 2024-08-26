from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from ..types import Renderable, Primitive


class RenderState:
    def __init__(self, *, root: "Renderable | Primitive", render_target: Literal["json", "html"], **kwargs):
        self.root = root
        self.render_target = render_target
        self.custom_data = kwargs
