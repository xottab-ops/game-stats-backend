from flask import Flask
from .config import Config
from .extensions import db, ma


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

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


    return app
