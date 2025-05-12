from sqlalchemy.sql import func

from app.dto import DeveloperGameStatsDTO, PublisherGameStatsDTO
from app.models import (
    Game,
    Developer,
    Publisher,
)
from app.extensions import db


def get_developers_aggregate():
    results = (
        db.session.query(
            Developer.id,
            Developer.name,
            func.min(Game.positive_rating),
            func.round(func.avg(Game.positive_rating) * 100) / 100,
            func.max(Game.positive_rating),
            func.min(Game.negative_rating),
            func.round(func.avg(Game.negative_rating) * 100) / 100,
            func.max(Game.negative_rating),
            func.min(Game.price),
            func.round(func.avg(Game.price) * 100) / 100,
            func.max(Game.price),
            func.count(Game.id),
        )
        .join(Game, Game.developer_id == Developer.id)
        .group_by(Developer.id)
        .order_by(func.count(Game.id).desc(), func.avg(Game.price).desc())
        .limit(20)
    )
    stats_objects = [DeveloperGameStatsDTO(*row) for row in results][:100]
    return stats_objects


def get_publisher_aggregate():
    results = (
        db.session.query(
            Publisher.id,
            Publisher.name,
            func.min(Game.positive_rating),
            func.round(func.avg(Game.positive_rating) * 100) / 100,
            func.max(Game.positive_rating),
            func.min(Game.negative_rating),
            func.round(func.avg(Game.negative_rating) * 100) / 100,
            func.max(Game.negative_rating),
            func.min(Game.price),
            func.round(func.avg(Game.price) * 100) / 100,
            func.max(Game.price),
            func.count(Game.id),
        )
        .join(Game, Game.publisher_id == Publisher.id)
        .group_by(Publisher.id)
        .order_by(func.count(Game.id).desc(), func.avg(Game.price).desc())
        .limit(20)
    )
    stats_objects = [PublisherGameStatsDTO(*row) for row in results][:100]
    return stats_objects
