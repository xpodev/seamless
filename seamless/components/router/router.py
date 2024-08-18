from json import dumps
from pathlib import Path
from typing import overload

from ...core import Empty, Component, JS

from .route import Route


HERE = Path(__file__).parent


class Router(Component):
    children: tuple[Route, ...] # type: ignore

    @overload
    def __init__(self, *, loading_component: type[Component] | None = None): ...
    @overload
    def __init__(self, *routes: Route, loading_component: type[Component] | None = None): ...
    
    def __init__(self, *, loading_component: type[Component] | None = None): # type: ignore
        self.loading_component = loading_component.__seamless_name__ if loading_component else None
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

        return Empty(init=JS(f"let routes = {dumps(routes)};{router_js}"), loading=self.loading_component)
