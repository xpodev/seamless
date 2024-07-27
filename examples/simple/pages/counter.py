from seamless import Div, Form, Input, Button, Component
from seamless.extra import State

class CounterPage(Component):
    def render(self):
        return Div(class_name="container")(
            Div(class_name="row")(
                Div(class_name="display-1 text-center")("Counter"),
                Div(class_name="display-6 text-center")("A simple counter page."),
            ),
            Div(class_name="row mt-4")(
                Div(class_name="lead col-12 text-center")("Current counter: ", State("counter").get()),
            ),
            Div(class_name="row")(
                Div(class_name="col-12 text-center")(
                    Div(class_name="btn-group")(
                        Div(class_name="btn btn-danger", on_click=State("counter").set("state - 1"))("Decrement"),
                        Div(class_name="btn btn-primary", on_click=State("counter").set("0"))("Reset"),
                        Div(class_name="btn btn-success", on_click=State("counter").set("state + 1"))("Increment"),
                    ),
                ),
                Div(class_name="col-12 text-center mt-4")(
                    Form(action="#", on_submit=self.submit)(
                        Input(type="hidden", name="counter_value", value=State("counter").get()),
                        Button(class_name="btn btn-primary", type="submit")("Submit"),
                    )
                ),
            ),
        )

    def submit(self, event):
        print("Form submitted!")
        print(event)

