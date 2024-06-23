from seamless import Div, Form, Input, Button
from . import BasePage


class CounterPage(BasePage, title="Seamless Counter Page"):
    def body(self):
        return (
            Div(class_name="container")(
                Div(class_name="row")(
                    Div(class_name="display-1 text-center")("Counter"),
                    Div(class_name="display-6 text-center")("A simple counter page."),
                ),
                Div(class_name="row mt-4")(
                    Div(class_name="lead col-12 text-center")("Current counter: 0")
                ),
                Div(class_name="row")(
                    Div(class_name="col-12 text-center")(
                        Div(class_name="btn-group")(
                            Div(class_name="btn btn-danger")("Decrement"),
                            Div(class_name="btn btn-success")("Increment"),
                        ),
                    ),
                    Div(class_name="col-12 text-center mt-4")(
                        Form(action="#", on_submit=self.submit)(
                            Input(type="hidden", name="counter_value", value=0),
                            Button(class_name="btn btn-primary", type="submit")("Submit"),
                        )
                    ),
                ),
            ),
        )
    
    def submit(self, event):
        print("Form submitted!")
        print(event)
