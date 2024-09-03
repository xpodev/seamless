from seamless import Component, Div, Nav, Button
from seamless.extensions import State
from seamless.extra.transports.socketio.transport import SocketIOTransport
from seamless.components.router import Router, Route, RouterLink
from pages import HomePage, CounterPage, BasePage

from .loading import Loading


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
                        Button(on_click=self.foo)(
                            "Click me!"
                        )
                    )
                ),
                Div(class_name="content flex-grow-1")(
                    Router(loading_component=Loading)(
                        Route(path="/", component=HomePage),
                        Route(path="/counter", component=CounterPage),
                    )
                ),
            ),
            title="Seamless",
        )

    def foo(self, event):
        print("foo")