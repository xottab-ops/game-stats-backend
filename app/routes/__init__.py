
from .games_routes import games_bp

def register_blueprints(app):
    app.register_blueprint(games_bp)
