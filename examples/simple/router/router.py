from seamless import Component, Script

from .route import Route

class Router(Component):
    def __init__(self, routes):
        for route in self.children:
            if not isinstance(route, Route):
                raise TypeError(f"Expected Route, got {type(route)}")

    def render(self):
        return Script(type="text/javascript")(
            f"""
            const routes = {self.children};
            const path = window.location.pathname;
            const route = routes.find(route => route.path === path);
            document.body.innerHTML = route.render();
            """
        )