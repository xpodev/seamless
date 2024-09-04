from typing import Optional
from pydom.errors import Error as PydomError

class Error(PydomError):
    """
    Base class for all seamless exceptions.
    """

    ...


class RenderError(Error):
    """
    Raised when an error occurs while rendering an element.
    """

    ...


class ClientError(Error):
    """
    Raised when an error occurs on the client side.
    Classes that inherit from this class will not be raised on the server side.
    """
    def __init__(self, *args: object, client_id: Optional[str] = None) -> None:
        super().__init__(*args)
        self.client_id = client_id
