from pydom import Component, Div, H3, Hr, Link
from pydom.page import Page as _Page


class Plugin(Component):
    def __init__(self, name, version) -> None:
        self.name = name
        self.version = version

    def render(self):
        return Div(
            classes="plugin",
        )(
            f"{self.name} v{self.version}",
        )


class PluginList(Component):
    def __init__(self, plugins=None) -> None:
        self.plugins = plugins if plugins is not None else []

    def render(self):
        return Div(
            classes="plugin-list",
        )(
            *[Plugin(plugin.name, plugin.version) for plugin in self.plugins],
        )


class Card(Component):
    def render(self):
        return Div(
            classes="card",
        )(
            *self.children,
        )


class CardTitle(Component):
    def render(self):
        return H3(
            classes="card-title",
        )(
            *self.children,
        )


class App(Component):
    def render(self):
        return Card(CardTitle("Card title"), Hr(), Div(*self.children))


class Page(_Page):
    def head(self):
        yield from super().head()
        yield Link(rel="stylesheet", href="/static/style.css")
