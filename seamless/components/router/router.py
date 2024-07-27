from json import dumps
from pathlib import Path

from seamless import Component, Div
from seamless.extra import JS, Empty

from .route import Route


HERE = Path(__file__).parent


class Router(Component):
    children: list[Route]

    def __init__(self):
        for route in self.children:
            if not isinstance(route, Route):
                raise TypeError(f"Expected Route, got {type(route)}")

    def render(self):
        routes = [
            {"path": route.path, "name": route.component.__seamless_name__}
            for route in self.children
        ]

        with open(HERE / "router.js", "r") as f:
            router_js = f.read()

        return Empty(init=JS(f"const routes = {dumps(routes)};{router_js}"))