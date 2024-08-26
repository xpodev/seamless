from seamless import Component, Div
from seamless.context import Context
from seamless.extra.events import EventsFeature

class Usage(Component, inject_render=True):
    def render(self, context: Context):
        events = context.get_feature(EventsFeature)

        return Div(
            f"Events: {len(events.DB.events)}"
        )