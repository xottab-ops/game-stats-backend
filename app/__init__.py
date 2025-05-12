from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db, ma
from .routes import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from app.models import (
            Category,
            Platform,
            Developer,
            Publisher,
            Game,
            PlatformGame,
            CategoryGame,
        )

        db.create_all()

    register_blueprints(app)

    return app
