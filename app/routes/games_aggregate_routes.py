from flask import Blueprint, jsonify, abort, make_response, request

from app.services.games_aggregate_service import get_developers_aggregate
from app.schemas import developer_schema

game_stats_bp = Blueprint('stats', __name__, url_prefix='/api/v1/stats')

@game_stats_bp.route('/', methods=['GET'])
def get_developer_stats():
    stats = get_developers_aggregate()
    return jsonify(developer_schema.dump(stats))