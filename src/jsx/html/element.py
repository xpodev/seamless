from typing import TYPE_CHECKING
from abc import abstractproperty

if TYPE_CHECKING:
    from jsx.types import ChildrenType


def class_name_mapper(class_name):
    return {
        "class": " ".join(
            class_name.split() if isinstance(class_name, str) else class_name
        )
    }


PROPS_MAP = {
    "class_name": class_name_mapper,
    "html_for": "for",
}


class Element:
    def __init__(self, *children: "ChildrenType", **kwargs):
        self.children = children
        self.props = kwargs

    @abstractproperty
    def tag_name(self) -> str:
        pass

    inline = False

    def props_dict(self):
        props_copy = self.props.copy()
        for key, value in PROPS_MAP.items():
            if key in props_copy:
                if callable(value):
                    props_copy.update(value(props_copy.pop(key)))
                else:
                    props_copy[value] = props_copy.pop(key)

        return props_copy
