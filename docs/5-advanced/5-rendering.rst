.. _rendering:

############
Rendering
############

When Seamless renders a component or an element, it does so in steps.

1. **Initialization**
   
   In this step, the render process initializes the ``RenderState`` object.

2. **Normalization**

   Then, the renderer will recursively walk through the component tree and normalize it to a tree of ``TreeNode`` object from the ``seamless.rendering.tree`` module.
   At this step, the renderer also applies the property transformers.

3. **Post-Render Transformation**

   After the tree is generated, it is passed through all the post-renderers that are registered in the current context.
   The post-renderers can modify the tree in any way they want, as long as the content can be rendered by the final renderer.

4. **Rendering**

   Finally, the tree is rendered to the target format (HTML, JSON, etc.).


.. note:: 
  Currently, only HTML and JSON rendering are supported.


.. _render-state:

Render State
############

The ``RenderState`` object is used to store the state of the rendering process.
It allows property transformers to pass information to the post-render transformers.

The ``RenderState`` object has the following attributes:

1. ``root``: The original renderable object that was passed to the renderer.
2. ``target_target``: A string representing the target format of the rendering process.
3. ``custom_data``: A dictionary that can be used to store custom data.


.. _accessing-render-state:

Accessing Render State
#######################


The render state can be accessed in the property transformers and post-render transformers by using the ``RenderState`` as a type annotation.

.. code-block:: python
    :caption: Accessing the render state in property transformers and post-render transformers

    from seamless.rendering.render_state import RenderState

    def my_property_transformer(key: str, value: Any, element: ElementNode, render_state: RenderState) -> None:
      # render_state contains the render state object

    def my_post_render_transformer(root: ElementNode, render_state: RenderState) -> None:
      # render_state contains the render state object


To store custom data in the render state, you can use the ``custom_data`` attribute of the render state object.
Simply set the desired key to the value you want to store.

.. important::
  To avoid conflicts with other transformers, it is recommended to use a unique key for the custom data.
  You can prefix the key with the name of your transformer to make it unique.

  For example, if you have a transformer named ``my_transformer``, you can store custom data like this:

  .. code-block:: python
      :caption: Storing custom data in the render state

      render_state.custom_data["my_transformer.custom_data"] = "My custom data"
