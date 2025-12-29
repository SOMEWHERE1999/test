from .response_code import ResponseCode


class APIException(Exception):
    def __init__(self, message="internal server error", code=ResponseCode.SERVER_ERROR, status_code=500):
        super().__init__(message)
        self.message = message
        self.code = code
        self.status_code = status_code

    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "data": {},
        }
