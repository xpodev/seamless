from pydantic import BaseModel
from seamless import Div, Form, Input, Button, Component
from seamless.core import SocketID
from seamless.extensions import State
from seamless.types.events import SubmitEvent


class Counter(BaseModel):
    counter_value: int


counter = State("counter", 0)


class CounterPage(Component):
    def render(self):
        return Div(class_name="container")(
            Div(class_name="row")(
                Div(class_name="display-1 text-center")("Counter"),
                Div(class_name="display-6 text-center")("A simple counter page."),
            ),
            Div(class_name="row mt-4")(
                Div(class_name="lead col-12 text-center")(
                    "Current counter: ", counter()
                ),
            ),
            Div(class_name="row")(
                Div(class_name="col-12 text-center")(
                    Div(class_name="btn-group")(
                        Div(class_name="btn btn-danger", on_click=counter("state - 1"))(
                            "Decrement"
                        ),
                        Div(class_name="btn btn-primary", on_click=counter("0"))(
                            "Reset"
                        ),
                        Div(
                            class_name="btn btn-success", on_click=counter("state + 1")
                        )("Increment"),
                    ),
                ),
                Div(class_name="col-12 text-center mt-4")(
                    Form(action="#", on_submit=self.submit)(
                        Input(type="hidden", name="counter_value", value=counter()),
                        Button(class_name="btn btn-primary", type="submit")("Submit"),
                    )
                ),
            ),
        )

    def submit(self, event: SubmitEvent[Counter], sid: SocketID):
        print("Form submitted!")
        print("socket id:", sid)
        print(event)
