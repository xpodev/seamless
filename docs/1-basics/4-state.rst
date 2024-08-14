.. _state:

#################
Client-Side State
#################

The client-side state is a way to store data in the client's browser. This data is
persistent across single page application (SPA) navigation and can be used to
store the application's state.

The state is persistent only in the current tab and is lost when the tab is closed or
refreshed.

Initializing the State
######################

Before creating any state, the state must to be initialized. This is done by calling the
``State.init`` method from ``seamless.extra``.

The ``State.init`` method initializes the state on the client side and adds the ``state`` object
in the seamless instance.

.. code-block:: python
    :caption: Initializing the state

    from seamless.extra import State

    class MyPage(Page):
        def body(self):
            return (
              State.init()
              *super().body()
            )


Creating a State
################

To create a state, create a new instance of the ``State`` class from ``seamless.extra``.

.. code-block:: python
    :caption: Creating a state

    from seamless.extra import State

    counter = State("counter", 0)

This will create a state with the name ``counter`` and the initial value of ``0``.

This state is now available to be used in the components.

Using a State
#############

To use a state, call the state object with the new value to update the state.

Setting the state is done by calling the state object with the new value as a JavaScript expression.
When setting a new value to the state, the current state is available as ``state`` in the expression.

Getting the state is done by calling the state object without any arguments.

.. code-block:: python
    :caption: Using a state

    class MyComponent(Component):
        def render(self):
            return Div(
                Button(
                    "Increment",
                    on_click=counter("state + 1")
                ),
                Span(counter())
            )

This will create a button that increments the counter state by one and displays the current value.

Accessing the State
###################

When creating a state, if the state name already exists, the existing state is returned.

This allows the same state to be accessed from different components without passing the state object.
