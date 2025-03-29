.. _components:

##########
Components
##########

.. toctree::
    :glob:
    :hidden:

    *

In HTML, we have tags like ``div``, ``span``, ``input``, ``button``, etc. which describes the structure of the UI.

In Seamless, we have `Elements` which represents the HTML tags. We also have ``Components`` which
is a wrapper around the `Elements` and can be used to create more complex UI structures.

`Components` can be used to create reusable UI structures. For example, an ``AppButton`` component can be created
which can be used throughout the application.

To create a component, we need to create a class which inherits from ``Component`` class and define the
``render`` method which returns the ``Element`` or ``Component`` which will be rendered.

The ``render`` method can return a single ``Element``, ``Component`` or one of the primitive types:
    * str
    * int
    * float
    * bool
    * None

| Except for the actual return value which can be only single ``Element``, ``Component`` or one of the primitive types, components and elements can have any number of children.
| To return multiple components from the ``render`` method, use the :ref:`fragment` component.
