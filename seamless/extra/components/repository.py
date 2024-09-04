from typing import Type

from pydom import Component


class ComponentsRepository:
    def __init__(self):
        self.components = {}

    def add_component(self, component: Type[Component], name: str):
        self.components[name] = component

    def get_component(self, component_name: str) -> Type[Component]:
        return self.components[component_name]
