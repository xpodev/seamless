from abc import abstractproperty

from ..components.component import Component


class Element:
    def __init__(
        self,
        *children: tuple["Element | Component | str"],
        class_name=None,
        html_for=None,
        inline=False,
        **kwargs
    ):
        self.children = [
            child.render() if isinstance(child, Component) else child
            for child in children
            if child is not None
        ]
        self.inline = inline
        kwargs["class"] = class_name
        kwargs["for"] = html_for
        self.props = kwargs

    @abstractproperty
    def tag_name(self) -> str:
        pass

    def to_json(self):
        return {
            "type": self.tag_name,
            "children": list(
                map(
                    lambda x: x.to_json() if isinstance(x, Element) else x,
                    self.children,
                )
            ),
            "props": self.props,
        }
