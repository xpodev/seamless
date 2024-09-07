from typing import Type

from pydom import Component


class Route(Component):
    def __init__(self, *, path, component: Type[Component]):
        self.path = path
        self.component = component

    def render(self):
        return None
