import logging
from logging.handlers import RotatingFileHandler
import os


def init_logger(app=None):
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "app.log")

    handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    logger = logging.getLogger("todolist")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(handler)

    if app:
        app.logger.handlers = logger.handlers
        app.logger.setLevel(logger.level)

    return logger
