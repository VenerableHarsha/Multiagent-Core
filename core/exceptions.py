class ToolError(Exception):
    """Raised when a tool encounters an error."""

    def __init__(self, message):
        self.message = message


class CoreError(Exception):
    """Base exception for all Core errors"""


class TokenLimitExceeded(CoreError):
    """Exception raised when the token limit is exceeded"""
