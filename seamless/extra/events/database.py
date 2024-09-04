from inspect import iscoroutinefunction
from typing import Any, Callable, Dict

from ...internal.utils import is_global

from .errors import EventNotFoundError


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


class EventsDatabase:

    def __init__(self):
        self.events: Dict[str, Action] = {}
        self.scoped_events: Dict[str, Dict[str, Action]] = {}
        self.actions_ids = dict[str | Callable, Action]()

    def add_event(self, action: Action, *, scope: str):
        try:
            return self.actions_ids[action.id]
        except KeyError:
            pass

        self.actions_ids[action.id] = action

        if is_global(action.action):
            self.events[action.id] = action

        self.scoped_events.setdefault(scope, {})[action.id] = action

        return action

    async def invoke_event(self, event: str, *data, scope: str):
        try:
            func = self.get_event(event, scope=scope)
        except KeyError:
            raise EventNotFoundError(event)

        return await func(*data)

    def release_actions(self, client_id: str):
        if client_id not in self.scoped_events:
            return

        del self.scoped_events[client_id]

    def get_event(self, event_id: str, *, scope: str):
        if event_id in self.events:
            return self.events[event_id]
        
        return self.scoped_events[scope][event_id]


