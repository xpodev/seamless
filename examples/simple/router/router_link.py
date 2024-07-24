from seamless import Component, A
from seamless.extra import JS


class RouterLink(Component):
    def __init__(self, *, to, **kwargs):
        self.to = to
        self.kwargs = kwargs

    def render(self):
        return A(
            href=self.to, on_click=JS(f"return this.navigateTo('{self.to}')"), **self.kwargs
        )(*self.children)
