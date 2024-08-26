.. _context:

#######
Context
#######

Context is an advanced feature of Seamless that allows you to customize the rendering process of Seamless components.

The default context is created using the ``Context.standard`` method and has the following features in order:

- **Component Repository**: A repository for storing components - this handles the ``component`` event and allows
  you to store and retrieve components after the initial render.

  .. code-block:: python

      from seamless.context import Context
      from seamless.extra.components import init_components

      context = Context()
      context.add_feature(init_components)

- **Events Feature**: This feature allows you to connect between HTML events and Python functions.

  .. code-block:: python

      from seamless.context import Context
      from seamless.extra.events import EventsFeature

      context = Context()
      context.add_feature(EventsFeature, claim_time=30)

- **State Feature**: This feature allows you to manage the state of components on the client-side.

  .. code-block:: python

      from seamless.context import Context
      from seamless.extra.state import init_state

      context = Context()
      context.add_feature(init_state)

The standard context also comes with the following :ref:`property transformers<property-transformers>` in order:

- **Class Transformer**: Changes the ``class_name`` property key to ``class`` and converts
  the value to a string if it is a list.

  .. code-block:: python

      from seamless.context import Context
      from seamless.extra.transformers.class_transformer import class_transformer

      context = Context()
      context.add_prop_transformer(*class_transformer())

- **Simple Transformer**: Converts the properties in :ref:`this list<props-rendering>` except for ``class_name``.

  .. code-block:: python

      from seamless.context import Context
      from seamless.extra.transformers.simple_transformer import simple_transformer

      context = Context()
      context.add_prop_transformer(*simple_transformer())

- **HTML Events Transformer**: Converts the properties keys from ``on_{event}`` to ``on{event}``.
  This works only when the property value is a string, ``JS`` and Python functions are handled by a different transformers.

  .. code-block:: python

      from seamless.context import Context
      from seamless.extra.transformers.html_events_transformer import html_events_transformer

      context = Context()
      context.add_prop_transformer(*html_events_transformer())

- **Dash Transformer**: Converts the properties keys from ``dash_case`` (AKA ``snake_case``) to ``kebab-case``.
  This works only for properties with primitive values.

  .. code-block:: python

      from seamless.context import Context
      from seamless.extra.transformers.dash_transformer import dash_transformer

      context = Context()
      context.add_prop_transformer(*dash_transformer())

- **Initialize Script Transformer**: Attaching the code in the ``init`` property to the ``seamless:init`` attribute.
  
    .. code-block:: python
  
        from seamless.context import Context
        from seamless.extra.transformers.js_transformer import init_transformer
  
        context = Context()
        context.add_prop_transformer(*init_transformer())

- **JS Transformer**: Attaching the code in all properties that start with ``on_`` to the corresponding HTML event.
  The transformer will add the ``attachEventListener`` method to the element inside the ``seamless:init`` attribute and
  remove the property from the element.

    .. code-block:: python

        from seamless.context import Context
        from seamless.extra.transformers.js_transformer import js_transformer

        context = Context()
        context.add_prop_transformer(*js_transformer())

- **Style Transformer**: Converts the properties with ``StyleObject`` as value to a css string.

    .. code-block:: python

        from seamless.context import Context
        from seamless.extra.transformers.style_transformer import style_transformer

        context = Context()
        context.add_prop_transformer(*style_transformer())