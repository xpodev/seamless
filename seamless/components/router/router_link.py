from ... import Component, A, JS


class RouterLink(Component):
    def __init__(self, *, to: str, **anchor_props):
        self.to = to
        self.anchor_props = anchor_props

    def render(self):
        return A(
            href=self.to, on_click=JS(f"event.preventDefault(); return seamless.navigateTo('{self.to}')"), **self.anchor_props
        )(*self.children)
