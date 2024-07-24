from json import dumps
from pathlib import Path

from seamless import Component, Div, Fragment
from seamless.internal import short_uuid
from seamless.extra import Source

from .route import Route


HERE = Path(__file__).parent


class Router(Component):
    children: list[Route]

    def __init__(self):
        for route in self.children:
            if not isinstance(route, Route):
                raise TypeError(f"Expected Route, got {type(route)}")

    def render(self):
        router_id = short_uuid(8)
        routes = [
            {"path": route.path, "name": route.component.__seamless_name__}
            for route in self.children
        ]

        with open(HERE / "router.js", "r") as f:
            router_js = f.read()

        return Fragment(
            Div(id=router_id, init=Source(
                f"const routerContent = document.getElementById('{router_id}');\n" \
                f"const routes = {dumps(routes)};\n" \
                f"{router_js}"
            ))
        )
