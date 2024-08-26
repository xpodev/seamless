from inspect import iscoroutinefunction, ismethod, signature
from typing import Any, Callable, TypeAlias
from threading import Timer

from ...core import SocketID
from .errors import ActionError
from ...internal.validation import wrap_with_validation
from ...context.request import request as _request, RequestType


ActionsMap: TypeAlias = dict[str, Callable | dict[str, Callable]]


class Action:
    def __init__(
        self,
        action: Callable,
        id: str,
    ):
        self.id = id
        self.action = action

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

    def add_event(self, action: Action, scope=None):
        try:
            return self.actions_ids[action.id]
        except KeyError:
            pass

        request = _request()

        if request.type == RequestType.HTTP:
            if request.id not in self._unclaimed_elements:
                self._unclaimed_elements[request.id] = []

            self._unclaimed_elements[request.id].append(action)

            def delete_unclaimed(claim_id):
                if claim_id in self._unclaimed_elements:
                    del self._unclaimed_elements[claim_id]

            timer = Timer(self.claim_time, delete_unclaimed, [request.id])
            self._unclaimed_elements_timeouts[request.id] = timer
            timer.start()
        else:
            self.actions_ids[action.id] = action

            if scope:
                if scope not in self.events:
                    self.events[scope] = {}

                self.events[scope][action.id] = action
            else:
                self.events[action.id] = action

        return action

    async def invoke_event(self, event: str, *data, scope=None):
        if scope and scope in self.events and event in self.events[scope]:
            func = self.events[scope][event]
        elif event in self.events:
            func = self.events[event]
        else:
            raise ActionError("Event not found")

        data = list(data)
        for index, param in enumerate(signature(func.action).parameters.values()):
            if param.annotation is SocketID:
                data.insert(index, scope)
        return await func(*data)

    def claim(self, claim_id, client_id):
        if claim_id not in self._unclaimed_elements:
            return

        self._unclaimed_elements_timeouts[claim_id].cancel()
        del self._unclaimed_elements_timeouts[claim_id]

        for action in self._unclaimed_elements[claim_id]:
            if ismethod(action.action):
                if client_id not in self.events:
                    self.events[client_id] = {}
                self.events[client_id][action.id] = action
            else:
                self.events[action.id] = action

        del self._unclaimed_elements[claim_id]

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
