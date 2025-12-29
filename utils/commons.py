from flask import request

from .response_code import RESPONSE_MESSAGES, ResponseCode


def parse_request_data():
    return request.get_json(silent=True) or {}


def success_response(data=None, message=None, code=ResponseCode.SUCCESS, status_code=200):
    return (
        {
            "code": code,
            "message": message or RESPONSE_MESSAGES.get(code, "success"),
            "data": data or {},
        },
        status_code,
    )


def error_response(message=None, code=ResponseCode.SERVER_ERROR, status_code=500):
    return (
        {
            "code": code,
            "message": message or RESPONSE_MESSAGES.get(code, "internal server error"),
            "data": {},
        },
        status_code,
    )
