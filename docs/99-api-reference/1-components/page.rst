.. _page-api-reference:

####
Page
####

.. py:currentmodule:: seamless.components

.. py:class:: Page
  :canonical: seamless.components.page.Page

  Inherits from :py:class:`~seamless.core.component.Component`.

  Methods
  =======

  .. py:method:: __init__(self, title=None, html_props=None, head_props=None, body_props=None)

    :param string title: The page's title
    :param dict html_props: The props to insert inside the ``html`` tag |br| **default**: ``{ "lang": "en" }``
    :param dict head_props: The props to insert inside the ``head`` tag |br| **default**: ``{}``
    :param dict body_props: The props to insert inside the ``body`` tag |br| **default**: ``{ "dir": "ltr" }``

  .. py:method:: head(self) -> Iterable[ChildType]
    
    The children that will be inside the ``head`` tag.

    :rtype: :py:type:`~seamless.types.ChildrenType`

  .. py:method:: body(self) -> Iterable[ChildType]
      
    The children that will be inside the ``body`` tag.
  
    :rtype: :py:type:`~seamless.types.ChildrenType`