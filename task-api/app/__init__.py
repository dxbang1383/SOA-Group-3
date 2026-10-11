
from flask import Flask

from .routes import api_bp


def create_app(test_config=None):
    """App quản lý sách"""
    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)

    app.register_blueprint(api_bp)
    return app
