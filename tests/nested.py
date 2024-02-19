from jsx import Component
from jsx.html import Div, H3, Hr


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

