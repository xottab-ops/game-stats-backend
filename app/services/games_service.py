from app.models import (
    Game,
    CategoryGame,
    PlatformGame,
)
from app.extensions import db


def get_games_info():
    query = Game.query.limit(100)
    return query.all()


def get_game_by_id(game_id):
    query = Game.query.filter_by(id=game_id).one_or_none()
    return query


def insert_game(data):

    game = Game(
        name=data["name"],
        developer_id=data["developer_id"],
        publisher_id=data["publisher_id"],
        release_date=data["release_date"],
        price=data.get("price", 0.0),
        positive_rating=data.get("positive_rating", 0),
        negative_rating=data.get("negative_rating", 0),
    )

    db.session.add(game)
    db.session.commit()

    # Добавляем связи с категориями, если есть
    if "category_ids" in data:
        for cat_id in data["category_ids"]:
            db.session.add(CategoryGame(game_id=game.id, category_id=cat_id))

    # Добавляем связи с платформами, если есть
    if "platform_ids" in data:
        for plat_id in data["platform_ids"]:
            db.session.add(PlatformGame(game_id=game.id, platform_id=plat_id))

    db.session.commit()
    return game


def update_game_by_id(id, data):
    game = Game.query.get(id)
    if game is None:
        return None

    for field in [
        "name",
        "developer_id",
        "publisher_id",
        "release_date",
        "price",
        "positive_rating",
        "negative_rating",
    ]:
        if field in data:
            setattr(game, field, data[field])

    if "category_ids" in data:
        CategoryGame.query.filter_by(game_id=game.id).delete()
        for cat_id in data["category_ids"]:
            db.session.add(CategoryGame(game_id=game.id, category_id=cat_id))

    if "platform_ids" in data:
        PlatformGame.query.filter_by(game_id=game.id).delete()
        for plat_id in data["platform_ids"]:
            db.session.add(PlatformGame(game_id=game.id, platform_id=plat_id))

    db.session.commit()
    return game


def delete_game_by_id(game_id):
    query = Game.query.filter_by(id=game_id).one_or_none()
    db.session.delete(query)
    db.session.commit()
