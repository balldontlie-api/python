
from typing import Optional

class BallDontLieException(Exception):
    def __init__(self, message: str, status_code: Optional[int] = None, response_data: Optional[dict] = None):
        super().__init__(message)
        self.status_code = status_code
        self.response_data = response_data

class AuthenticationError(BallDontLieException):
    pass

class RateLimitError(BallDontLieException):
    pass

class ValidationError(BallDontLieException):
    pass

class NotFoundError(BallDontLieException):
    pass

class ServerError(BallDontLieException):
    pass