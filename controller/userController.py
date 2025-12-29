from flask import Blueprint

from models.user import User
from utils import ResponseCode, error_response, parse_request_data, success_response

user_bp = Blueprint("user", __name__)


@user_bp.route("/", methods=["GET"])
def list_users():
    users = User.query.order_by(User.created_at.desc()).all()
    return success_response([user.to_dict() for user in users])


@user_bp.route("/", methods=["POST"])
def create_user():
    data = parse_request_data()
    username = (data.get("username") or "").strip()
    password_hash = (data.get("password_hash") or "").strip()

    if not username or not password_hash:
        return error_response("username and password_hash are required", ResponseCode.INVALID_PARAMS, 400)

    existing = User.query.filter_by(username=username).first()
    if existing:
        return error_response("username already exists", ResponseCode.INVALID_PARAMS, 400)

    user = User(username=username, password_hash=password_hash)
    from models import db

    db.session.add(user)
    db.session.commit()
    return success_response(user.to_dict(), "created", status_code=201)
