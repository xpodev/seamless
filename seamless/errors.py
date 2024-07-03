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


class ActionError(Error):
    """
    Raised when an error occurs while invoking an action.
    """
    ...