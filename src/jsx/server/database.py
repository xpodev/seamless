from typing import Callable
from uuid import uuid4 as uuid
from ..components import Component
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

# TODO: Add remove element when socket is closed

class ElementsDatabase:
    def __init__(self):
        self.component_events: dict[str, dict[str, Callable]] = {}
        self.component_ids = TwoWayDict()

    def add_component_event(self, component: Component | Element, event: str, callback: Callable):
        if component not in self.component_ids:
            component_id = uuid()
            self.component_ids[component] = component_id

        component_id = self.component_ids[component]

        self.component_events[component_id] = self.component_events.get(component_id, {})
        self.component_events[component_id][event] = callback

    def get_component_event(self, component: Component | Element, event: str) -> Callable:
        component_id = self.component_ids[component]
        return self.component_events[component_id].get(event)
    
    def invoke_component_event(self, component_id: str, event: str, *data):
        callback = self.component_events[component_id].get(event)
        if callback:
            callback(*data)