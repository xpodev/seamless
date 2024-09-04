from seamless import Component, Div, Table, Th, Tr, Td, H2
from seamless.context import Context
from seamless.extra.events import EventsFeature


class Usage(Component, inject_render=True):
    def render(self, context: Context):
        events = context.get_feature(EventsFeature)
        total_scoped = sum(len(scope) for scope in events.DB.scoped_events.values())

        return Div(
            H2(f"Global Events - Total: {len(events.DB.events)}"),
            Table(
                Tr(
                    Th("Event ID"),
                ),
                *(
                    Tr(
                        Td(event_id),
                    )
                    for event_id in events.DB.events
                ),
            ),
            H2(f"Actions - Total: {total_scoped}"),
            Table(
                Tr(
                    Th("Scope ID"),
                    Th("Actions IDs"),
                ),
                *(
                    Tr(
                        Td(scope),
                        Td(", ".join(actions.keys()))
                    )
                    for scope, actions in events.DB.scoped_events.items()
                )
            ),
        )
