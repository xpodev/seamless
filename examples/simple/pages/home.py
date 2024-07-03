from seamless import Div
from . import BasePage


class HomePage(BasePage, title="Seamless Home"):
    def body(self):
        return (
            Div(class_name="container")(
                Div(class_name="row")(
                    Div(class_name="display-1 text-center")("Welcome to Seamless!"),
                    Div(class_name="display-6 text-center")(
                        "A Python library for building web pages using Python."
                    ),
                ),
                Div(class_name="row mt-4")(
                    Div(class_name="lead col-12 text-center")(
                        "Current counter: 0"
                    )
                ),
            ),
        )
