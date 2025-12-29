class ResponseCode:
    SUCCESS = 0
    INVALID_PARAMS = 400
    NOT_FOUND = 404
    SERVER_ERROR = 500


RESPONSE_MESSAGES = {
    ResponseCode.SUCCESS: "success",
    ResponseCode.INVALID_PARAMS: "invalid parameters",
    ResponseCode.NOT_FOUND: "resource not found",
    ResponseCode.SERVER_ERROR: "internal server error",
}
