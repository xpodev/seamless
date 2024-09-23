.. _style-object:

############
Style Object
############

The ``StyleObject`` class is used to create reusable styles for components.
It is a dictionary-like object that can be used to store CSS properties and values.

Usage
#####

To create a new style object, create a new instance of the ``StyleObject`` class from ``seamless.styling``.

.. code-block:: python
    :caption: Creating a style object

    from seamless.styling import StyleObject

    style = StyleObject(
        background_color="red",
        color="white"
    )

This will create a style object with the properties ``background_color`` and ``color``.

To use the style object, pass it as the ``style`` prop to the component.

.. code-block:: python
    :caption: Using a style object

    from seamless import Component, Div

    class App(Component):
        def render(self):
            return Div(style=style)(
                "Hello, world!"
            )

This will create an inline style with the properties from the style object.

.. code-block:: html
    :caption: Style object output

    <div style="background-color: red; color: white;">Hello, world!</div>

Properties
##########

The ``StyleObject`` class has all the properties from the CSS specification.
The only difference is that the properties are written in snake_case instead of kebab-case.