from flask import Flask, render_template
from flask_cors import CORS

from config import Config
from controller import todo_bp, user_bp
from models import db
from models.todolist import TodoStatus
from utils import init_logger


def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)
    init_logger(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(todo_bp, url_prefix="/api/todos")
    app.register_blueprint(user_bp, url_prefix="/api/users")

    @app.route("/")
    def index():
        return render_template("index.html", statuses=TodoStatus.choices())

    return app
