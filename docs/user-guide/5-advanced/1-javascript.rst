.. _javascript:

##########
JavaScript
##########

Embedding JavaScript in Seamless is easy and straightforward.
You can include JavaScript code in your Seamless components using the ``JavaScript`` class or
its alias ``JS``.

Usage
#####

To include JavaScript code in your Seamless component, use the ``JavaScript`` class or its alias ``JS``.

.. code-block:: python
    :caption: Including JavaScript code in a Seamless component

    from seamless import Component, JS

    class App(Component):
        def render(self):
            return Div(init=JS("alert('Hello, world!')"))


This will include the JavaScript code ``alert('Hello, world!')`` in the component.

The JavaScript class can be used in two ways:
- code: The JavaScript code to include in the component.
- path: The path to a JavaScript file to include in the component.
  
.. code-block:: python
    :caption: Including JavaScript code from a file

    from seamless import Component, JS

    class App(Component):
        def render(self):
            return Div(init=JS(file="path/to/file.js"))

.. _the-init-property:

The init Property
#################

Seamless elements have an ``init`` property that is used to include JavaScript code in the component.
The JavaScript code will be executed when the component is mounted to the DOM.

Additional Info
###############

When using the ``JavaScript`` class, the JavaScript code will be executed inside a function that is bounded to
the HTML element. This means that you can access the HTML element using the ``this`` keyword.

Also, the function is called with the seamless context as the first argument named ``seamless``.

.. code-block:: javascript
    :caption: Seamless function wrapper

    function (seamless: { instance: Seamless }) {
        // JavaScript code
    }

Seamless Context
################

The Seamless context is an extensible object that is used to store all the extensions and data of the Seamless application.
It is passed as the first argument to the JavaScript function that is included in the component.

The default seamless context includes the following properties:
- ``instance``: The Seamless instance.

When creating a new functionality for the app, it is recommended to store it in the seamless context instead of
using global variables.

.. important:: 
    Do not confuse the seamless **context** with the seamless **instance**.

    The seamless **context** is the object responsible for holding all the data and extensions of the Seamless application.
    It is OK to add new properties to the seamless context.

    The seamless **instance** is the object responsible for managing the components, rendering, and updating the DOM.
    It is also responsible for handling all the events and interactions between the server and the client.
    There is no need to add new properties to the seamless instance and it is not recommended to do so.

.. code-block:: javascript
    :caption: Creating a new functionality in the seamless context

    function popup(message, timeout) {
        const popupFrame = document.createElement("div");
        popupFrame.innerHTML = message;
        document.body.appendChild(popupFrame);
        setTimeout(() => {
            document.body.removeChild(popupFrame);
        }, timeout);
    }

    seamless.popup = popup;

This will create a new function called ``popup`` in the seamless context that can be accessed from any ``JavaScript`` class code.
