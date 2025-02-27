from pydantic import BaseModel
from seamless import Div, Form, Input, Button, Component
from seamless.extra.transports.client_id import ClientID
from seamless.extensions import State
from seamless.types.events import SubmitEvent


class Counter(BaseModel):
    counter_value: int


counter = State("counter", 0)


class CounterPage(Component):
    def render(self):
        return Div(classes="container")(
            Div(classes="row")(
                Div(classes="display-1 text-center")("Counter"),
                Div(classes="display-6 text-center")("A simple counter page."),
            ),
            Div(classes="row mt-4")(
                Div(classes="lead col-12 text-center")(
                    "Current counter: ", counter()
                ),
            ),
            Div(classes="row")(
                Div(classes="col-12 text-center")(
                    Div(classes="btn-group")(
                        Div(classes="btn btn-danger", on_click=counter("state - 1"))(
                            "Decrement"
                        ),
                        Div(classes="btn btn-primary", on_click=counter("0"))(
                            "Reset"
                        ),
                        Div(
                            classes="btn btn-success", on_click=counter("state + 1")
                        )("Increment"),
                    ),
                ),
                Div(classes="col-12 text-center mt-4")(
                    Form(action="#", on_submit=self.submit)(
                        Input(type="hidden", name="counter_value", value=counter()),
                        Button(classes="btn btn-primary", type="submit")("Submit"),
                    )
                ),
                Button(
                    classes="btn btn-primary", type="submit", on_click=global_submit
                )("Submit 2"),
            ),
        )

    def submit(self, event: SubmitEvent[Counter], sid: ClientID):
        print("Form submitted!")
        print("socket id:", sid)
        print(event)


def global_submit(event, sid: ClientID):
    print("Global submit!")
    print("socket id:", sid)
    print(event)
