from seamless import Component, Div, Nav, Button
from seamless.context.context import Context
from seamless.styling import StyleSheet
from seamless.extensions import State, SocketIOTransport
from seamless.components.router import Router, Route, RouterLink
from pages import HomePage, CounterPage, BasePage, UserPage
from components.loading import Loading
from components.usage import Usage


class App(Component):
    def render(self):
        return BasePage(
            State.init(),
            SocketIOTransport.init(),
            Div(classes="d-flex flex-column h-100")(
                Div(classes="d-flex justify-content-between")(
                    Nav(classes="navbar navbar-expand-lg navbar-light bg-light")(
                        RouterLink(to="/", classes="navbar-brand")("Home"),
                        RouterLink(to="/counter", classes="navbar-brand")("Counter"),
                    ),
                    Div(
                        Button(on_click=foo, style=StyleSheet(border_radius="5px", background_color="red"))(
                            "Click me!"
                        )
                    )
                ),
                Div(classes="content flex-grow-1")(
                    Router(loading_component=Loading)(
                        Route(path="/", component=HomePage),
                        Route(path="/counter", component=CounterPage),
                        Route(path="/user/{user_id:int}", component=UserPage),
                        Route(path="/usage", component=Usage),
                    )
                ),
            ),
            title="Seamless",
        )

def foo(event, context: Context):
    print("foo")