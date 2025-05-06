from sqlalchemy.sql import func

from app.dto import DeveloperGameStatsDTO, PublisherGameStatsDTO
from app.models import (
    Game, Developer, Publisher,
)
from app.extensions import db


def get_developers_aggregate():
    results = (
        db.session.query(
            Developer.id,
            Developer.name,
            func.min(Game.positive_rating),
            func.avg(Game.positive_rating),
            func.max(Game.positive_rating),
            func.min(Game.negative_rating),
            func.avg(Game.negative_rating),
            func.max(Game.negative_rating),
            func.min(Game.price),
            func.avg(Game.price),
            func.max(Game.price),
            func.count(Game.id)
        )
        .join(Game, Game.developer_id == Developer.id)
        .group_by(Developer.id)
        .all()
    )
    stats_objects = [
        DeveloperGameStatsDTO(*row)
        for row in results
    ][:100]
    return stats_objects

def get_publisher_aggregate():
    results = (
        db.session.query(
            Publisher.id,
            Publisher.name,
            func.min(Game.positive_rating),
            func.avg(Game.positive_rating),
            func.max(Game.positive_rating),
            func.min(Game.negative_rating),
            func.avg(Game.negative_rating),
            func.max(Game.negative_rating),
            func.min(Game.price),
            func.avg(Game.price),
            func.max(Game.price),
            func.count(Game.id)
        )
        .join(Game, Game.publisher_id == Publisher.id)
        .group_by(Publisher.id)
        .all()
    )
    stats_objects = [
        PublisherGameStatsDTO(*row)
        for row in results
    ][:100]
    return stats_objects