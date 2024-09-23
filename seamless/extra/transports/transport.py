from typing import Any, Set

from pydom.context import Context
from pydom.utils.functions import random_string

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

    _client_ids: Set[str] = set()

    @staticmethod
    def create_client_id() -> str:
        client_id = random_string(24)
        TransportFeature._client_ids.add(client_id)
        return client_id
    
    @staticmethod
    def claim_client_id(client_id: str):
        TransportFeature._client_ids.remove(client_id)
    