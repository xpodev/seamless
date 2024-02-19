from abc import abstractproperty

from ..components.component import Component


PROPS_MAP = {
    "class_name": "class",
    "html_for": "for",
}


class Element:
    def __init__(
        self,
        *children: tuple["Element | Component | str"],
        **kwargs
    ):
        self.children = children
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
                    lambda elem: elem.to_json() if isinstance(elem, (Element, Component)) else elem,
                    self.children,
                )
            ),
            "props": self.props_dict(),
        }

    def props_dict(self):
        props_copy = self.props.copy()
        for key, value in PROPS_MAP.items():
            if key in props_copy:
                props_copy[value] = props_copy.pop(key)

        return props_copy