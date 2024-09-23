.. _empty:

#####
Empty
#####

The ``Empty`` element is a special element that is used to add JavaScript code into the page without
rendering any HTML.

Usage
#####

To use the ``Empty`` element, create a new instance of the ``Empty`` class from ``seamless.core``.

.. code-block:: python
    :caption: Using the Empty element

    from seamless import Component, JS
    from seamless.extra import Empty

    class App(Component):
        def render(self):
            return Div(
                Empty(init=JS("alert('Hello, world!')"))
            )


This will include the JavaScript code ``alert('Hello, world!')`` in the component without rendering any HTML.

Children
########

The ``Empty`` element can have children, they will be rendered as children of the parent of the ``Empty`` element.


Under the Hood
##############

In the initial render, the ``Empty`` element will render an HTML element with the tag ``seamless:empty``,
which will be removed from the DOM after the :ref:`Seamless instance <seamless-instance>` is initialized.