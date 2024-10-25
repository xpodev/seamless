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

        def save_email(self, event: SubmitEvent):
            user = get_user(self.email)
            user.email = event.data["email"]
            user.save()

In this example, we bind the ``submit`` event of the form to the ``save_email`` method of the user.

.. code-block:: python

    Form(on_submit=self.save_email)

When the form is submitted, the ``save_email`` method is called with the event data.

Scoping
#######

When binding a Python function to an event, there is a difference between using a method and a function.

When using any bound method, the method is scoped to the client, which means the action is only available
to the user who requested the component. This is done by storing the method inside a database specific
to the user.

Users who try to invoke the method will get an ``Event not found`` error if they are not the owner of the component.

When using a function that is not a method, the function will be stored to the global database, which means
the action is available to all users.

This is useful when you want to create a global action that is available to all users.

.. code-block:: python
    :caption: Scoping of events

    from random import randint
    from seamless import Component, Button, Div

    global_id = randint(0, 1000)

    def global_action(event_data):
        print("Global Action")
        print(global_id) # All users will have the same ID
        

    class App(Component):
        def __init__(self):
            self.id = randint(0, 1000)

        def render(self):
            return Div(Button(on_click=self.scoped_action)(
                "Scoped Action",
            ),Button(on_click=global_action)(
                "Global Action",
            ))

        def scoped_action(self, event_data):
            print("Scoped Action")
            print(self.id) # Each user will have a different ID


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
        this.addEventListener(EVENT_NAME, (event) => {
            // JavaScript code
        });
    }

Injecting Parameters
####################

You can inject parameters into the event handler by using annotations in the function signature.

.. note:: 
    The injectable parameters are always passed as keyword arguments. |br|
    Event functions can not have positional-only arguments.

For example, you can access the client ID by adding a parameter to the event handler function
with the ``ClientID`` type from the ``seamless.extra.transports`` module.

.. code-block:: python
    :caption: Accessing the socket ID

    from seamless.extra.transports import ClientID

    def on_event(self, event_data: SubmitEvent, cid: ClientID):
        print("Client ID:", cid)

In the standard context, the following injectable parameters are available:

- **Client ID**: The unique ID of the client that triggered the event.
- **Context**: The current :ref:`Seamless context <context>`.