from ...core import Component


class Route(Component):
    def __init__(self, *, path, component: type[Component]):
        self.path = path
        self.component = component

    def render(self):
        return None
