###########
CSS Modules
###########

.. toctree::
    :glob:
    :hidden:

    *

CSS Modules are a way to write CSS that's scoped to a single css file, rather than globally.
It's a way to write CSS that's more maintainable and easier to understand.

Usage
#####

To use CSS Modules in a component, import the ``CSS`` object from the ``seamless.styling`` module.
Then, use the ``CSS`` to import your css files.

.. code-block:: css

    /* card.css */

    .card {
        background-color: white;
        border: 1px solid black;
        border-radius: 5px;
        padding: 10px;
    }


.. code-block:: python

    from seamless.styling import CSS

    styles = CSS.module("./card.css")

    class MyComponent(Component):
        def render(self, css):
            return Div(class_name=styles.card)(
                "Hello, world!"
            )

This will generate a class name that is unique to this css file, and apply the styles to that class name.
This way, you can be sure that your styles won't conflict with other styles in your app.

When importing the same css file in multiple components, the class name will be the same across all components.