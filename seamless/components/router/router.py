from json import dumps
from pathlib import Path
from typing import Optional, Tuple, overload, Type

from pydom import Component

from ...core import Empty, JS
from ...extra.components import component_name
from .route import Route


HERE = Path(__file__).parent


class Router(Component):
    children: Tuple[Route, ...]  # type: ignore

    @overload
    def __init__(self, *, loading_component: Optional[Type[Component]] = None): ...
    @overload
    def __init__(
        self, *routes: Route, loading_component: Optional[Type[Component]] = None
    ): ...

    def __init__(self, *, loading_component: Optional[Type[Component]] = None):  # type: ignore
        self.loading_component = (
            component_name(loading_component) if loading_component else None
        )
        for route in self.children:
            if not isinstance(route, Route):
                raise TypeError(f"Expected Route, got {type(route)}")

    def render(self):
        routes = [
            {"path": route.path, "name": component_name(route.component)}
            for route in self.children
        ]

        with open(HERE / "router.js", "r") as f:
            router_js = f.read()

        return Empty(
            init=JS(f"let routes = {dumps(routes)};{router_js}"),
            loading=self.loading_component,
        )
