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

        try:
            transport = context.get_feature(TransportFeature)
        except KeyError:
            raise ValueError(
                "ComponentsFeature requires a TransportFeature in the context."
                "Please add it before adding the ComponentsFeature."
            )

        transport.event.on("component", self.get_component)

    async def get_component(self, client_id: str, component_name: str, props=None, *_):
        props = props or {}
        cls = self.DB.get_component(component_name)

        try:
            component = cls(**props)
        except TypeError:
            raise ClientError(
                f"Invalid props for component {component_name}", client_id=client_id
            )

        return render_json(
            component, context=self.context, **{"transports.client_id": client_id}
        )


def component_name(component: Type[Component]) -> Optional[str]:
    return getattr(component, "__seamless_name__", None)
