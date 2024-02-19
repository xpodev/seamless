from abc import abstractmethod
import typing

if typing.TYPE_CHECKING:
    from ..html.element import Element


class Component:
    def __init__(self, *children: "Component | Element | str", **props):
        self.children = children
        self.props = props

    @abstractmethod
    def render(self) -> "Element | str":
        raise NotImplementedError(f"{type(self).__name__}.render() is not implemented")

    def to_json(self):
        return self.render().to_json()