from inspect import iscoroutinefunction, ismethod
from typing import Any, Callable, TypeAlias
from uuid import uuid4 as uuid
from threading import Timer

from seamless.errors import ActionError
from seamless.internal import validate_data, TwoWayDict
from .request import request as _request, RequestType


ActionsMap: TypeAlias = dict[str, Callable] | dict[str, dict[str, Callable]]


class Action:
    def __init__(
        self,
        action: Callable,
    ):
        self._id = str(uuid())
        self.action = action  # TODO: make wrapper for action for data validation

    @property
    def id(self):
        return self._id

    async def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if iscoroutinefunction(self.action):
            return await self.action(*args, **kwargs)
        return self.action(*args, **kwargs)


class ElementsDatabase:

    def __init__(self, *, claim_time=20.0):
        self.events: ActionsMap = {}
        self.actions_ids = dict[str | Callable, Action]()
        self._unclaimed_elements = dict[str, list[Action]]()
        self._unclaimed_elements_timeouts = dict[str, Timer]()
        self.claim_time = claim_time

    def add_event(self, callback: Callable, scope=None):
        if callback in self.actions_ids:
            return self.actions_ids[callback]

        request = _request()
        action = Action(callback)

        if request.type == RequestType.HTTP:
            if request.id not in self._unclaimed_elements:
                self._unclaimed_elements[request.id] = []

            self._unclaimed_elements[request.id].append(action)

            def delete_unclaimed(claim_id):
                del self._unclaimed_elements[claim_id]

            timer = Timer(self.claim_time, delete_unclaimed, [request.id])
            self._unclaimed_elements_timeouts[request.id] = timer
            timer.start()
        else:
            self.actions_ids[callback] = action
            self.actions_ids[action.id] = action

            if scope:
                if scope not in self.events:
                    self.events[scope] = {}

                self.events[scope][action.id] = callback
            else:
                self.events[action.id] = callback

        return action

    async def invoke_event(self, event: str, *data, scope=None):
        if scope and scope in self.events and event in self.events[scope]:
            return await self.events[scope][event](*data)

        if event in self.events:
            return await self.events[event](*data)

        raise ActionError("Event not found")

    def claim_http_actions(self, http_id, socket_id):
        if http_id not in self._unclaimed_elements:
            return

        self._unclaimed_elements_timeouts[http_id].cancel()
        del self._unclaimed_elements_timeouts[http_id]

        for action in self._unclaimed_elements[http_id]:
            if ismethod(action.action):
                if socket_id not in self.events:
                    self.events[socket_id] = {}
                self.events[socket_id][action.id] = action
            else:
                self.events[action.id] = action

        del self._unclaimed_elements[http_id]

    def release_actions(self, socket_id: str):
        if socket_id not in self.events:
            return

        del self.events[socket_id]

    @property
    def _all_unclaimed(self):
        all_unclaimed = {}
        for subscriptable_list in self._unclaimed_elements.values():
            all_unclaimed.update((e.id, e) for e in subscriptable_list)

        return all_unclaimed


DB = ElementsDatabase(claim_time=30)
