
from .user_routes import bp as user_bp

def register_blueprints(app):
    app.register_blueprint(user_bp)
