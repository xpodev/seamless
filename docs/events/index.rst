##################
Events and Actions
##################

.. toctree::
    :glob:
    :hidden:

    *

One of the most powerful features of Seamless is the ability to connect between
Python function and methods to the HTML events. This allows you to create interactive
web pages that respond to user input.

The following example demonstrates how to submit a form to the server:

.. code-block:: python
    :caption: Submitting a form to the server

    from seamless import Component, Form, Label, Div, Input, Button
    from seamless.types import SubmitEvent

    class User(Component):
        def __init__(self, name: str, email: str):
            self.age = age
            self.email = email

        def render(self):
            return Form(on_submit=self.save_email)(
                Div(f"Update the email for {name}"),
                Label(html_for="email")(
                    "Age: ",
                ),
                Input(type="email", value=self.email, name="email", id="email"),
                Button(type="submit")(
                    "Submit Email",
                ),
            )

        def save_email(self, event_data: SubmitEvent):
            user = get_user(self.email)
            user.email = event_data["email"]
            user.save()