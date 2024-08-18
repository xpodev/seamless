class Error(Exception):
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

    ...
