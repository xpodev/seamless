from seamless import Div, Component
from seamless.extensions import State
from components.clock import Clock


class HomePage(Component):
    def render(self):
        return Div(classes="container")(
            Div(classes="row")(
                Div(classes="display-1 text-center")("Welcome to Seamless!"),
                Div(classes="display-6 text-center")(
                    "A Python library for building web pages using Python."
                ),
            ),
            Div(classes="row mt-4")(
                Div(classes="lead col-12 text-center")("Current counter: ", State("counter").get()),
            ),
            Clock(),
        )
