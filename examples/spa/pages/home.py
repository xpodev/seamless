from seamless import Div, Component, Input, Button, JS
from seamless.extensions import State

search_user = State("search_user")

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
            Div(classes="row mt-4")(
                "Search User: ",
                Input(type="text", on_change=search_user("this.value")),
                Button(on_click=JS(f"seamless.navigateTo('/user/' + {search_user})"))("Search"),
            ),
        )
