from seamless import Component, A
from seamless.extra import Source


class RouterLink(Component):
    def __init__(self, *, to, **kwargs):
        self.to = to
        self.kwargs = kwargs

    def render(self):
        return A(
            href=self.to, on_click=Source(f"return this.navigateTo('{self.to}')"), **self.kwargs
        )(*self.children)
