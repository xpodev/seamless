from typing import Any

from pydom.context import Context

from ..feature import Feature
from .dispatcher import dispatcher
from .subscriptable import event


class TransportFeature(Feature):
    def __init__(self, context: Context) -> None:
        super().__init__(context)

    @event
    @staticmethod
    def connect(client_id: str, request: Any) -> None:
        pass

    @event
    @staticmethod
    def disconnect(client_id: str) -> None:
        pass

    @event
    @staticmethod
    def error(error: Exception) -> None:
        pass

    @dispatcher
    @staticmethod
    def event(client_id: str, /, *args: Any) -> Any:
        pass
