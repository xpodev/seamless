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
            Div(classes="d-flex flex-column h-100")(
                Div(classes="d-flex justify-content-between")(
                    Nav(classes="navbar navbar-expand-lg navbar-light bg-light")(
                        RouterLink(to="/", classes="navbar-brand")("Home"),
                        RouterLink(to="/counter", classes="navbar-brand")("Counter"),
                    ),
                    Div(
                        Button(on_click=self.foo)(
                            "Click me!"
                        )
                    )
                ),
                Div(classes="content flex-grow-1")(
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