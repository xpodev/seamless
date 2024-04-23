from inspect import iscoroutinefunction
from typing import Any, Callable, TYPE_CHECKING
from uuid import uuid4 as uuid
from threading import Timer

from jsx.internal import validate_data
from .request import request, RequestType

if TYPE_CHECKING:
    from ..html import Element


class TwoWayDict(dict):
    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        if value in self:
            del self[value]
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

    def __delitem__(self, key):
        dict.__delitem__(self, self[key])
        dict.__delitem__(self, key)

    def __len__(self):
        """Returns the number of connections"""
        return dict.__len__(self) // 2


class SubscriptableElement:
    def __init__(
        self,
        element: "Element",
        socket_id: str = None,
    ):
        self.component = element
        self._id = str(uuid())
        self._socket_id = socket_id
        self._events = {}

    def set_socket_id(self, socket_id: str):
        if self._socket_id is None:
            self._socket_id = socket_id
        else:
            raise ValueError("Socket ID already set")

    def add_event(self, event: str, callback: Callable):
        self._events[event] = callback

    @property
    def id(self):
        return self._id

    @property
    def socket_id(self):
        return self._socket_id

    @property
    def events(self):
        return self._events.keys()

    async def __call__(self, event: str, *args: Any, **kwargs: Any) -> Any:
        if event in self._events:
            callback = self._events[event]
            args = validate_data(callback, *args)
            if iscoroutinefunction(callback):
                return await callback(*args, **kwargs)
            return callback(*args, **kwargs)


class ElementsDatabase:

    def __init__(self, *, claim_time=20.0):
        self.elements = dict[str, SubscriptableElement]()
        self.element_ids = TwoWayDict()
        self._unclaimed_elements = dict[str, list[SubscriptableElement]]()
        self._unclaimed_elements_timeouts = dict[str, Timer]()
        self.claim_time = claim_time

    def add_element_event(self, element: "Element", event: str, callback: Callable):
        if element in self.element_ids:
            subscriptable = self.get_element(element)
        else:
            subscriptable = SubscriptableElement(element)
            self.element_ids[element] = subscriptable.id
            if request().type == RequestType.WS:
                self._register_element(subscriptable, request().socket_id)
            else:
                if self._request.id not in self._unclaimed_elements:
                    self._unclaimed_elements[self._request.id] = []

            self._unclaimed_elements[self._request.id].append(subscriptable)

            def delete_unclaimed(http_id):
                for subscriptable in self._unclaimed_elements[http_id]:
                    del self.element_ids[subscriptable.id]

                del self._unclaimed_elements[http_id]

            timer = Timer(self.claim_time, delete_unclaimed, [self._request.id])
            self._unclaimed_elements_timeouts[self._request.id] = timer
            timer.start()

        subscriptable.add_event(event, callback)

    def get_element(self, element: "Element"):
        element_id = self.element_ids[element]
        return self.all[element_id]

    async def invoke_element_event(self, element_id: str, socket_id: str, event: str, *data):
        subscriptable = self.elements[element_id]
        if subscriptable:
            if not subscriptable.socket_id == socket_id:
                raise Exception("Element not found")

            await subscriptable(event, *data)

    def claim_http_elements(self, http_id, socket_id):
        if http_id not in self._unclaimed_elements:
            return

        self._unclaimed_elements_timeouts[http_id].cancel()
        del self._unclaimed_elements_timeouts[http_id]

        for subscriptable in self._unclaimed_elements[http_id]:
            self._register_element(subscriptable, socket_id)

        del self._unclaimed_elements[http_id]

    def release_elements(self, socket_id: str):
        for element_id, subscriptable in list(self.elements.items()):
            if subscriptable.socket_id == socket_id:
                del self.elements[element_id]
                del self.element_ids[element_id]

    def _register_element(self, subscriptable: SubscriptableElement, socket_id: str):
        subscriptable.set_socket_id(socket_id)
        self.elements[subscriptable.id] = subscriptable

    @property
    def _all_unclaimed(self):
        all_unclaimed = {}
        for subscriptable_list in self._unclaimed_elements.values():
            all_unclaimed.update((e.id, e) for e in subscriptable_list)

        return all_unclaimed

    @property
    def all(self):
        all_elements = self.elements.copy()
        all_elements.update(self._all_unclaimed)
        return all_elements

    @property
    def _request(self):
        return request()


DB = ElementsDatabase(claim_time=30)
