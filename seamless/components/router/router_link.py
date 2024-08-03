from seamless import Component, A, JS


class RouterLink(Component):
    def __init__(self, *, to, **kwargs):
        self.to = to
        self.kwargs = kwargs

    def render(self):
        return A(
            href=self.to, on_click=JS(f"event.preventDefault(); return seamless.navigateTo('{self.to}')"), **self.kwargs
        )(*self.children)
