from seamless import Component, Div, Nav
from seamless.extra import State
from seamless.components.router import Router, Route, RouterLink
from pages import HomePage, CounterPage, BasePage


class App(Component):
    def render(self):
        return BasePage(
            State.init(),
            Div(
                Nav(class_name="navbar navbar-expand-lg navbar-light bg-light")(
                    RouterLink(to="/", class_name="navbar-brand")("Home"),
                    RouterLink(to="/counter", class_name="navbar-brand")("Counter"),
                ),
                Div(class_name="content")(
                    Router(
                        Route(path="/", component=HomePage),
                        Route(path="/counter", component=CounterPage),
                    )
                ),
            ),
            title="Seamless",
        )
