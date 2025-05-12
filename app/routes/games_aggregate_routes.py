from flask import Blueprint, jsonify, abort, make_response, request

from app.schemas.publisher_schema import publisher_schema
from app.services.games_aggregate_service import (
    get_developers_aggregate,
    get_publisher_aggregate,
)
from app.schemas import developer_schema

game_stats_bp = Blueprint("stats", __name__, url_prefix="/api/v1/stats")


@game_stats_bp.route("/developers", methods=["GET"])
def get_developer_stats():
    stats = get_developers_aggregate()
    return jsonify({"stats": developer_schema.dump(stats)})


@game_stats_bp.route("/publishers", methods=["GET"])
def get_publisher_stats():
    stats = get_publisher_aggregate()
    return jsonify({"stats": publisher_schema.dump(stats)})
