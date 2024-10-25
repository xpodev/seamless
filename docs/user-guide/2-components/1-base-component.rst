.. _base-component:

##############
Base Component
##############

The ``Component`` class is an abstract class that provides a base implementation for any seamless component.
It provides a ``children`` property that is a tuple of the components that are contained within the component.

.. note:: 
  The ``children`` property is not a list, but a tuple. This means that it is immutable and cannot be modified directly.

  It is possible to modify the children property by creating a new tuple and assigning it to the children property.

.. code-block:: python
    :caption: Card example
    :name: card-component

    # card.py

    from seamless import Component, Div

    class Card(Component):
        def __init__(self, title=None):
            self.title = title

        def render(self):
            return Div(class_name="card")(
              self.title and Div(class_name="card-title")(
                self.title
              ),
              Div(class_name="card-content")(
                *self.children
              )
            )

The ``Component`` class is responsible for creating and initializing the children property, 
which means it is not passed as a parameter to the subclass's __init__ function, but it is accessible inside it.

.. code-block:: python
    :caption: Children property access in __init__

    from seamless import Component, Div

    class Card(Component):
        def __init__(self, title=None):
            self.number_of_children = len(self.children) # self.children is accessible in __init__
            ...

        def render(self):
          ...

Since it is possible to get a component by name from the server, it's best to avoid using the same class name
for different components.
By default, the name of the component is the name of the class, but it can be changed by passing the ``name``
parameter as keyword argument when inheriting from ``Component``.

.. code-block:: python
    :caption: Custom name for the component

    from seamless import Component

    class MyComponent(Component, name="MyCustomComponent"):
        ...

Props
#####

Components can have props which are passed as kwargs to the ``__init__`` method of the component.
The props are handled inside the ``__init__`` method and can be used to render the component.

.. important:: 
    Props has to be passed as keyword arguments to the component.
    Positional arguments are handled as children.

The most common way of handling props is to store them as instance variables and use them in the ``render`` method.

.. code-block:: python
    :caption: Handling props

    from seamless import Component

    class AppButton(Component):
        def __init__(self, type: str):
            self.style = Style(background_color=f"var(--color-{type})")

        def render(self):
            return Button(style=self.style)(
                *self.children
            )

    button = AppButton(type="primary")(
        "Click me"
    )


It is possible to mark the component as ``dataclass`` which will automatically handle the props,
create the ``__init__`` method with the correct signature and store the props as instance variables.

.. code-block:: python
    :caption: Using dataclass to handle props

    from seamless import Component

    @dataclass
    class AppButton(Component):
        color: str

        def render(self):
            return Button(style=Style(background_color=f"var(--color-{self.color}"))(
                *self.children
            )

    button = AppButton(color="primary")(
        "Click me"
    )

The following names are reserved and cannot be used as props:
    * children

Children
########

In Seamless, children are the components or elements that are nested inside another component or element.

To add children to a component, pass them as positional arguments, use the ``children`` prop or call the
component with the children as arguments. (See :ref:`syntax`)

.. code-block:: python
    :caption: Adding children to a component

    from seamless import Component, Div

    class Card(Component):
        def __init__(self, title=None):
            self.title = title

        def render(self):
            return Div(class_name="card")(
                Div(class_name="card-header")(
                    self.title
                ),
                Div(class_name="card-body")(
                    *self.children
                )
            )

    card = Card(title="Card title")(
        "Card content"
    )
