from app.extensions import db, ma

from app.models import (
    Game,
    Category,
    Platform,
    Developer,
    Publisher,
)

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category

class PlatformSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Platform

class DeveloperSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Developer

class PublisherSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Publisher


class GameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Game
        include_fk = True
        load_instance = True
        sqla_session = db.session

    developer = ma.Nested(DeveloperSchema)
    publisher = ma.Nested(PublisherSchema)

    categories = ma.Nested(CategorySchema, many=True)
    platforms = ma.Nested(PlatformSchema, many=True)

game_cschema = GameSchema()
games_cschema = GameSchema(many=True)