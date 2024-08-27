from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..context.base import ContextBase


class Feature:
    def __init__(self, context: "ContextBase") -> None:
        self.context = context
