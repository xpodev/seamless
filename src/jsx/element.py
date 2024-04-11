from typing import TYPE_CHECKING, Iterable, TypeVar, Generic, Unpack
from abc import abstractmethod

from .types import Primitive, Renderable

from .server.database import DB

if TYPE_CHECKING:
    from jsx.types import ChildrenType


PropsType = TypeVar("PropsType")


def _class_name_mapper(class_name):
    if isinstance(class_name, list):
        class_name = " ".join(class_name)

    class_name = str(class_name)
    return {"class": " ".join(class_name.split())}


_PROPS_MAP = {
    "class_name": _class_name_mapper,
    "html_for": "for",
}


class Element(Generic[PropsType]):
    def __init__(
        self,
        *args: "ChildrenType",
        children: Iterable[Renderable | Primitive] = [],
        **kwargs: Unpack[PropsType],
    ):
        self.children = list(args or children)
        self.props = kwargs

    @property
    @abstractmethod
    def tag_name(self) -> str:
        pass

    inline = False

    def props_dict(self):
        props_copy = self.props.copy()
        for key, value in _PROPS_MAP.items():
            if key in props_copy:
                if callable(value):
                    props_copy.update(value(props_copy.pop(key)))
                else:
                    props_copy[value] = props_copy.pop(key)

        jsx_events = []
        for key, value in list(props_copy.items()):
            if key.startswith("on_") and callable(value):
                props_copy[key] = None
                key = key.removeprefix("on_")
                DB.add_element_event(self, key, value)
                jsx_events.append(key)
            if value is None or value is False:
                del props_copy[key]

        if len(jsx_events) > 0:
            props_copy["slarf:id"] = DB.element_ids[self]
            props_copy["slarf:events"] = ",".join(jsx_events)

        return props_copy

    def __call__(self, *children: "ChildrenType"):
        self.children = children
        return self
