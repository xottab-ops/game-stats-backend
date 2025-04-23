from flask import Flask
from .config import Config
from .extensions import db, ma
from .routes import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    register_blueprints(app)

    return app
