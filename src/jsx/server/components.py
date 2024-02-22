from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from jsx import Component


class ComponentsRepository:
    def __init__(self):
        self.components = {}

    def add_component(self, component: "Component"):
        self.components[component.__name__] = component

    def get_component(self, component_name: str) -> "Component":
        return self.components[component_name]


COMPONENTS_REPOSITORY = ComponentsRepository()
