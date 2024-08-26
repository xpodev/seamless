.. _route-api-reference:

#####
Route
#####

.. py:currentmodule:: seamless.components.router

.. py:class:: Route
  :canonical: seamless.components.router.route.Route

  Inherits from :py:class:`~seamless.core.component.Component`.

  Methods
  =======

  .. py:method:: __init__(self, path: str, component: type[Component])
  
    :param string path: The path of the page
    :param ``Component`` component: The component to render when the path is matched
