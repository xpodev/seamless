from seamless import Component, Div, H3, Hr, Link, Button
from seamless.components import Page as _Page
from seamless.extra import JS


class Plugin(Component):
    def __init__(self, name, version) -> None:
        self.name = name
        self.version = version

    def render(self):
        return Div(
            f"{self.name} v{self.version}",
            class_name="plugin",
        )


class PluginList(Component):
    def __init__(self, plugins=None) -> None:
        self.plugins = plugins if plugins is not None else []

    def render(self):
        return Div(
            *[Plugin(plugin.name, plugin.version) for plugin in self.plugins],
            class_name="plugin-list",
        )


class Card(Component):
    def render(self):
        return Div(
            *self.children,
            class_name="card",
        )


class CardTitle(Component):
    def render(self):
        return H3(
            *self.children,
            class_name="card-title",
        )


class App(Component):
    def render(self):
        return Card(
            CardTitle("Card title"),
            Hr(),
            Div("Card content"),
        )


class Page(_Page):
    def head(self):
        yield from super().head()
        yield Link(rel="stylesheet", href="/static/style.css")


class AlertButton(Component):
    def render(self):
        return Button(on_click=JS("alert('Button clicked')"))(
            "Click me",
        )