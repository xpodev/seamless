import inspect
from typing import TYPE_CHECKING, ClassVar, Optional, Type

from pydom import Component
from pydom.context import Context
from pydom.context.feature import Feature
from pydom.rendering import render_json

from ...errors import ClientError
from .repository import ComponentsRepository
from ..transports.transport import TransportFeature

if TYPE_CHECKING:

    class _Component(Component):
        __seamless_name__: ClassVar[str]


class ComponentsFeature(Feature):
    def __init__(self, context: Context) -> None:
        super().__init__(context)
        self.DB = ComponentsRepository()

        original_init_subclass = Component.__init_subclass__

        @classmethod
        def __init_subclass__(
            cls: Type["_Component"],
            *,
            name: Optional[str] = None,
            inject_render: bool = False,
            **kwargs,
        ) -> None:
            if not inspect.isabstract(cls):

                cls.__seamless_name__ = (
                    cls.__dict__.get("__seamless_name__", None) or name or cls.__name__
                )
                self.DB.add_component(cls, cls.__seamless_name__)

                if inject_render:
                    cls.render = context.inject(cls.render)

            original_init_subclass.__func__(cls, **kwargs)  # type: ignore

        Component.__init_subclass__ = __init_subclass__

        if isinstance(self.context, Context):
            self.context.on("component", self.get_component)

    def get_component(self, sid: str, name: str, props=None):
        props = props or {}
        cls = self.DB.get_component(name)
        try:
            component = cls(**props)
        except TypeError:
            raise ClientError(f"Invalid props for component {name}")

        return render_json(component, context=self.context, events_scope=sid)
