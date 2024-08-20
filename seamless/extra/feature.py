from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..context import Context


class Feature:
    def __init__(self, context: "Context") -> None:
        self.context = context
