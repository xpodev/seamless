from seamless import Component, Div, Nav, Button
from seamless.context.context import Context
from seamless.styling import StyleObject
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
            Div(class_name="d-flex flex-column h-100")(
                Div(class_name="d-flex justify-content-between")(
                    Nav(class_name="navbar navbar-expand-lg navbar-light bg-light")(
                        RouterLink(to="/", class_name="navbar-brand")("Home"),
                        RouterLink(to="/counter", class_name="navbar-brand")("Counter"),
                    ),
                    Div(
                        Button(on_click=foo, style=StyleObject(border_radius="5px", background_color="red"))(
                            "Click me!"
                        )
                    )
                ),
                Div(class_name="content flex-grow-1")(
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