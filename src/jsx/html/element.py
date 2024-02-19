from abc import abstractproperty

from ..components.component import Component


class Element:
    def __init__(
        self,
        *children: tuple["Element | Component | str"],
        class_name=None,
        html_for=None,
        **kwargs
    ):
        self.children = children
        kwargs["class"] = class_name
        kwargs["for"] = html_for
        self.props = kwargs

    @abstractproperty
    def tag_name(self) -> str:
        pass

    inline = False

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
