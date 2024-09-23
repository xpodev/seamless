.. _base-component-api-reference:

#########
Component
#########

.. py:class:: Component
  :module: seamless
  :canonical: seamless.core.component.Component

  The base class for all components.

  .. py:method:: __init__(*children: ChildType, **props: Any)
    
    :param children: The children of the component
    :type children: :py:type:`~seamless.types.ChildrenType`
    :param props: The props of the component
    :type props: :py:type:`~seamless.types.PropsType`

  .. py:method:: render(self) -> RenderResult
      :abstractmethod:

      Renders the component. |br|
      This method is an abstract method that must be implemented by the subclass.
  
      :rtype: :py:type:`~seamless.types.RenderResult`