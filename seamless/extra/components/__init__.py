from typing import TYPE_CHECKING

from ...core.component import Component
from ...errors import ClientError
from ...rendering import render_json

from ..feature import Feature
from .repository import ComponentsRepository

if TYPE_CHECKING:
    from ...context import Context


class ComponentsFeature(Feature):
    def __init__(self, context: "Context") -> None:
        super().__init__(context)
        self.DB = ComponentsRepository()

        original_init_subclass = Component.__init_subclass__

        @classmethod
        def __init_subclass__(
            cls: type[Component], *, name: str | None = None, inject_render: bool = False, **kwargs
        ) -> None:
            if cls is not Component:

                cls.__seamless_name__ = name or cls.__name__
                self.DB.add_component(cls, cls.__seamless_name__)

                if inject_render:
                    cls.render = context.inject(cls.render)

            original_init_subclass.__func__(cls, **kwargs)  # type: ignore

        Component.__init_subclass__ = __init_subclass__

        context.on("component", self.get_component)

    def get_component(self, sid: str, name: str, props=None):
        props = props or {}
        cls = self.DB.get_component(name)
        try:
            component = cls(**props)
        except TypeError:
            raise ClientError(f"Invalid props for component {name}")

        return render_json(component, context=self.context, events_scope=sid)
