from flask import Blueprint

from models import db
from models.todolist import Todo, TodoStatus
from utils import (
    APIException,
    ResponseCode,
    error_response,
    parse_request_data,
    success_response,
)


todo_bp = Blueprint("todo", __name__)


@todo_bp.route("/", methods=["GET"])
def list_todos():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return success_response([todo.to_dict() for todo in todos])


@todo_bp.route("/", methods=["POST"])
def create_todo():
    data = parse_request_data()
    title = (data.get("title") or "").strip()
    status = data.get("status", TodoStatus.TODO)

    if not title:
        return error_response("title is required", ResponseCode.INVALID_PARAMS, 400)
    if status not in TodoStatus.choices():
        return error_response("invalid status", ResponseCode.INVALID_PARAMS, 400)

    todo = Todo(title=title, status=status)
    db.session.add(todo)
    db.session.commit()
    return success_response(todo.to_dict(), "created", status_code=201)


@todo_bp.route("/<int:todo_id>", methods=["PUT", "PATCH"])
def update_todo(todo_id: int):
    data = parse_request_data()
    todo = Todo.query.get(todo_id)
    if not todo:
        return error_response("todo not found", ResponseCode.NOT_FOUND, 404)

    title = data.get("title")
    status = data.get("status")

    if title is not None:
        title = title.strip()
        if not title:
            return error_response("title is required", ResponseCode.INVALID_PARAMS, 400)
        todo.title = title

    if status is not None:
        if status not in TodoStatus.choices():
            return error_response("invalid status", ResponseCode.INVALID_PARAMS, 400)
        todo.status = status

    db.session.commit()
    return success_response(todo.to_dict(), "updated")


@todo_bp.route("/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id: int):
    todo = Todo.query.get(todo_id)
    if not todo:
        return error_response("todo not found", ResponseCode.NOT_FOUND, 404)

    db.session.delete(todo)
    db.session.commit()
    return success_response({}, "deleted")


def handle_api_exception(error: APIException):
    return error.to_dict(), error.status_code


todo_bp.register_error_handler(APIException, handle_api_exception)
