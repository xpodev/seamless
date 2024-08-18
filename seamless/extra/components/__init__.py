from typing import TYPE_CHECKING

from ...core.component import Component
from ...errors import ClientError
from ...rendering.json import to_dict

from .repository import ComponentsRepository

if TYPE_CHECKING:
    from ...context import Context


def init_components(ctx: "Context"):
    COMPONENTS_REPOSITORY = ComponentsRepository()

    original_init_subclass = Component.__init_subclass__

    @classmethod
    def __init_subclass__(
        cls: type[Component], *, name: str | None = None, **kwargs
    ) -> None:
        if cls is not Component:

            cls.__seamless_name__ = name or cls.__name__
            COMPONENTS_REPOSITORY.add_component(cls, cls.__seamless_name__)

        original_init_subclass.__func__(cls, **kwargs) # type: ignore

    Component.__init_subclass__ = __init_subclass__

    def get_component(sid: str, name: str, props=None):
        props = props or {}
        cls = COMPONENTS_REPOSITORY.get_component(name)
        try:
            component = cls(**props)
        except TypeError:
            raise ClientError(f"Invalid props for component {name}")
        
        return to_dict(component)

    ctx.on("component", get_component)
