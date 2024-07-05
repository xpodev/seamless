from seamless import Component, A


class RouterLink(Component):
    def __init__(self, *, to, **kwargs):
        self.to = to
        self.kwargs = kwargs

    def render(self):
        return A(
            href=self.to, on_click=f"return navigateTo('{self.to}')", **self.kwargs
        )(*self.children)
