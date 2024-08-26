.. _router-api-reference:

######
Router
######

.. py:currentmodule:: seamless.components.router

.. py:class:: Router
  :canonical: seamless.components.router.router.Router

  Inherits from :py:class:`~seamless.core.component.Component`.

  Methods
  =======

  .. py:method:: __init__(self, *, loading_component: type[Component] | None = None)
  .. py:method:: __init__(self, *routes: Route, loading_component: type[Component] | None = None)
    :no-index:

    :param ``Component`` loading_component: The component to show between components loading
    :param ``Route`` routes: The routes to include in the application - can also passed as children of the Router component
