class InvalidTickerError(Exception):
    """Raised when an invalid ticker is provided."""
    pass

class InvalidDataTypeError(Exception):
    """Raised when an invalid data type is requested."""
    pass

class APIConnectionError(Exception):
    """Raised when there is an error connecting to an API."""
    pass
