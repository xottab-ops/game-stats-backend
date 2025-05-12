from .games_routes import games_bp
from .games_aggregate_routes import game_stats_bp
from .healthcheck_route import healthcheck_bp


def register_blueprints(app):
    app.register_blueprint(games_bp)
    app.register_blueprint(game_stats_bp)
    app.register_blueprint(healthcheck_bp)
