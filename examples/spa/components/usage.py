from seamless import Component, Div, Table, Th, Tr, Td, Span, Details, Summary
from seamless.context import Context
from seamless.extra.events import EventsFeature
from seamless.extra.events.database import Action
from seamless.styling import CSS

styles = CSS.module("./usage.css")


class ActionTable(Component):
    def __init__(self, actions: dict[str, Action]):
        self.actions = actions

    def render(self):
        return Table(class_name=styles.table)(
            Tr(
                Th("Index"),
                Th("Event ID"),
                Th("Module Name"),
                Th("Function Name"),
            ),
            *(
                Tr(
                    Td(index + 1),
                    Td(event_id),
                    Td(func.action.__module__),
                    Td(func.action.__name__),
                )
                for index, (event_id, func) in enumerate(self.actions.items())
            ),
        )


class Usage(Component, inject_render=True):
    def render(self, context: Context):
        events = context.get_feature(EventsFeature)
        total_scoped = sum(len(scope) for scope in events.DB.scoped_events.values())

        return Div(class_name="p-4")(
            Details(
                Summary(
                    Span(class_name="h2")(
                        f"Global Events - Total: {len(events.DB.events)}"
                    )
                ),
                ActionTable(actions=events.DB.events),
            ),
            Details(
                Summary(Span(class_name="h2")(f"Actions - Total: {total_scoped}")),
                *(
                    Details(
                        Summary(Span(class_name="h3")(f"Scope: {scope}")),
                        Div(
                            ActionTable(actions=events.DB.scoped_events[scope]),
                        ),
                    )
                    for scope in events.DB.scoped_events
                ),
            ),
        )
