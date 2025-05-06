from flask import Blueprint, jsonify, abort, make_response, request

from app.services.games_service import (
    get_games_info,
    get_game_by_id,
    delete_game_by_id,
    insert_game,
    update_game_by_id,
)
from app.schemas import games_cschema, game_cschema

games_bp = Blueprint("games", __name__, url_prefix="/api/v1/games")


@games_bp.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


@games_bp.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad Request"}), 400)


@games_bp.route("", methods=["GET"])
def get_games():
    games = get_games_info()
    return jsonify({"games": games_cschema.dump(games)})


@games_bp.route("/<int:id>", methods=["GET"])
def get_game_from_id(id):
    game = get_game_by_id(id)
    if game is None:
        abort(404)
    return jsonify(game_cschema.dump(game))


@games_bp.route("", methods=["POST"])
def create_game():
    if (
        not request.json
        or "name" not in request.json
        or "developer_id" not in request.json
        or "publisher_id" not in request.json
        or "release_date" not in request.json
    ):
        abort(400)

    new_game_data = request.get_json()

    # Значения по умолчанию
    new_game_data.setdefault("price", 0.0)
    new_game_data.setdefault("positive_rating", 0)
    new_game_data.setdefault("negative_rating", 0)

    created_game = insert_game(new_game_data)
    return jsonify({"game": game_cschema.dump(created_game)}), 201


@games_bp.route("/<int:id>", methods=["PUT"])
def update_game(id):
    game = get_game_by_id(id)
    if game is None or not request.json:
        abort(404)

    data = request.get_json()

    if "name" in data and not isinstance(data["name"], str):
        abort(400)
    if "developer_id" in data and not isinstance(data["developer_id"], int):
        abort(400)
    if "publisher_id" in data and not isinstance(data["publisher_id"], int):
        abort(400)
    if "price" in data and not isinstance(data["price"], (int, float)):
        abort(400)
    if "positive_rating" in data and not isinstance(data["positive_rating"], int):
        abort(400)
    if "negative_rating" in data and not isinstance(data["negative_rating"], int):
        abort(400)
    if "release_date" in data and not isinstance(data["release_date"], str):
        abort(400)

    updated_game = update_game_by_id(id, data)
    return jsonify({"game": game_cschema.dump(updated_game)})


@games_bp.route("/<int:id>", methods=["DELETE"])
def delete_game_from_id(id):
    game = get_game_by_id(id)
    if game is None:
        abort(404)
    delete_game_by_id(id)
    return jsonify({"success": True})
