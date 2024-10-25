.. _transformers:

############
Transformers
############

Seamless provides a way to transform the elements before rendering them to HTML and JSON.

There are 2 types of transformers:

1. **Property Transformers**: These transformers are used to transform a specific property of an element.
2. **Post-Render Transformers**: These transformers are used to transform the entire HTML content after it is rendered.


.. _property-transformers:

Property Transformers
#####################

Property transformers are used to transform a specific property of an element.
You can think of them as renderers for specific properties.
For example, you can use a property transformer to give a class to each element that has inline styles.

.. important:: 
    Property transformers are only available for elements and not for components.
    This is because property transformers are applied after the whole component is rendered to a normalized tree.

The following example demonstrates how to use a property transformer to give a class to each element that has inline styles:

.. code-block:: python

    # my_component.py

    from seamless import Component, Div, Span

    class MyComponent(Component):
        def render(self):
            return Div(
                Span(style="color: red")("Hello"),
                Span(style="color: blue")("World"),
            )


.. code-block:: python
    :caption: Property transformer to give a class to each element that has inline styles

    # style_transformer.py

    from seamless.extra import property_transformer
    from seamless.rendering.render_state import RenderState
    from seamless.rendering.tree import ElementNode

    @property_transformer("style")
    def add_class_to_inline_styles(key, value, element: ElementNode, render_state: RenderState):
        class_name = uuid4().hex
        if value:
            element.props["class"] = f"{class_name} {element.props.get('class', '')}"

        render_state.custom_data["css_string"] = render_state.custom_data.get("css_string", "") + f".{class_name} {{{value}}}"
        del element.props[key]


The ``property_transformer`` decorator takes the property name as an argument or a matcher function that returns ``True``
if the transformer should be applied.
Matcher functions are function with the following signature:

.. code-block:: python
    :caption: Matcher function signature

    def matcher(key: str, value: Any) -> bool: ...

The property transformer function takes the following arguments:

1. ``key``: The property name.
2. ``value``: The property value.
3. ``element``: The element node object - an instance of the ``ElementNode`` class from ``seamless.rendering.tree`` module.

.. code-block:: python
    :caption: Property transformer function signature

    from seamless.rendering.tree import ElementNode

    def transformer(key: str, value: Any, element: ElementNode) -> None: ...

.. _post-render-transformers:

Post-Render Transformers
########################

Post-render transformers are used to transform the entire HTML content after it is rendered.
For example, if we want to add the CSS from the property transformer to the HTML content, we can use a post-render transformer.

The following example demonstrates how to use a post-render transformer to add the CSS from the property transformer to the HTML content:

.. code-block:: python
    :caption: Using a post-render transformer to add the CSS from the property transformer to the HTML content

    # style_transformer.py

    from seamless import Style
    from seamless.extra import property_transformer, post_render_transformer
    from seamless.rendering.render_state import RenderState
    from seamless.rendering.tree import ElementNode

    @property_transformer("style")
    def add_class_to_inline_styles(key, value, element, render_state: RenderState):
        class_name = uuid4().hex
        if value:
            element.props["class"] = f"{class_name} {element.props.get('class', '')}"

        render_state.custom_data["css_string"] = render_state.custom_data.get("css_string", "") + f".{class_name} {{{value}}}"
        del element.props[key]

    @post_render_transformer()
    def add_css_to_html(root: ElementNode, render_state: RenderState):
        if "css_string" not in render_state.custom_data:
            return

        root.get_by_tag("head").append(
            ElementNode(
                tag_name="style",
                children=[render_state.custom_data["css_string"]]
            )
        )
