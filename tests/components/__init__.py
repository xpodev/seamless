from jsx import Component, ContainerComponent
from jsx.html import Div, H3, Hr


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


class Card(ContainerComponent):
    def render(self):
        return Div(
            *self.children,
            class_name="card",
        )


class CardTitle(Component):
    def __init__(self, *children):
        self.children = children

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
