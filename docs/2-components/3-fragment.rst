.. _fragment:

########
Fragment
########

``Fragment`` is an empty component that can be used to wrap a list of elements. It is a common pattern
in Seamless to return multiple elements from a component without adding an extra node to the DOM.

.. code-block:: python
    :caption: Using Fragment

    from seamless import Fragment, Component, Div

    class MyComponent(Component):
        def render(self):
            return Fragment(
                Div("Hello"),
                Div("World")
            )
