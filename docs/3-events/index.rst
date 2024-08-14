.. _events:

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

Using JavaScript in Events
##########################

You can use JavaScript code in the events by using the ``JS`` class from the ``seamless`` module.
The JavaScript code will be executed in the client-side when the event is triggered.

Inside the JavaScript code, you can use the ``event`` variable to access the original event object.

When using the ``JS`` class as an event handler, the JavaScript code will be added in the :ref:`init <the-init-property>` property
of the element and will register the event listener.

.. code-block:: javascript
    :caption: Event function wrapper

    function (seamless) {
        this.addEventListener(EVENT_NAME, function(event) {
            // JavaScript code
        });
    }

Accessing the Socket ID
#######################

Sometimes you may need to access the socket ID of the client that triggered the event.
You can access the socket ID by adding a parameter to the event handler function
with the ``SocketID`` type from the ``seamless.core`` module.

The socket id can be used to send messages to the client that triggered the event.

.. code-block:: python
    :caption: Accessing the socket ID

    from seamless.core import SocketID

    def on_event(self, event_data: SubmitEvent, socket_id: SocketID):
        print(socket_id)
