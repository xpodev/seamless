from seamless import Component, Div
from seamless.styling import CSS

styles = CSS.module("./loading.css")


class Loading(Component):
    def render(self):
        return Div(classes="d-flex align-items-center justify-content-center h-100")(
            Div(
                classes=f"{styles.spinner}",
            ),
        )
