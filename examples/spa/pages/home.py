from seamless import Div, Component, Input, Button, JS
from seamless.extensions import State

search_user = State("search_user")

class HomePage(Component):
    def render(self):
        return Div(class_name="container")(
            Div(class_name="row")(
                Div(class_name="display-1 text-center")("Welcome to Seamless!"),
                Div(class_name="display-6 text-center")(
                    "A Python library for building web pages using Python."
                ),
            ),
            Div(class_name="row mt-4")(
                Div(class_name="lead col-12 text-center")("Current counter: ", State("counter").get()),
            ),
            Div(class_name="row mt-4")(
                "Search User: ",
                Input(type="text", on_change=search_user("this.value")),
                Button(on_click=JS(f"seamless.navigateTo('/user/' + {search_user})"))("Search"),
            ),
        )
