.. _data-validation:

###############
Data Validation
###############

Seamless makes it easy to validate data when linking actions between the client and the server
using the `pydantic <https://docs.pydantic.dev/>`_ library.

If ``pydantic`` is installed, Seamless will automatically validate the data sent between the client and the server.

Here is an example of how to use ``pydantic`` to validate data:

.. code-block:: python
  :caption: Example of using Pydantic to validate data

  from pydantic import BaseModel
  from seamless import Component, Form, Input, Button
  from seamless.types.events import SubmitEvent

  class MyForm(Form):
      class UserLogin(BaseModel):
          username: str
          password: str
          remember_me: bool

      def render(self):
          return Form(on_submit=self.on_submit)(
              Input(name="username"),
              Input(name="password"),
              Button(type="submit")(
                  "Submit"
              )
          )

      def on_submit(self, event: SubmitEvent[UserLogin]):
          print(event.data)

This will create a form with the fields ``username``, ``password``, and ``remember_me``, and a submit button.

When the form is submitted, the data will be validated using the ``UserLogin`` model from ``pydantic``.
If the data is invalid, an error will be returned to the client.

.. note:: 
  If ``pydantic`` is not installed, Seamless will not validate the data sent between the client and the server
  but will convert the data from ``dict`` to an object.