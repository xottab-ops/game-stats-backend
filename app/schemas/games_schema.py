from app.extensions import db, ma
from marshmallow import fields, post_dump

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

    _links = fields.Method('get_links')

    categories = ma.Nested(CategorySchema, many=True)
    platforms = ma.Nested(PlatformSchema, many=True)

    def get_links(self, obj):
        return {
            "self": {"href": f"/games/{obj.id}"},
            "update": {"href": f"/games/{obj.id}", "method": "PUT"},
            "delete": {"href": f"/games/{obj.id}", "method": "DELETE"},
        }

    @post_dump()
    def wrap_with_links(self, data, many, **kwargs):
        if many:
            return {
                "games": data,
                "_links": {
                    "self": {"href": "/games"},
                    "create": {"href": "/games", "method": "POST"}
                }
            }
        return data

game_cschema = GameSchema()
games_cschema = GameSchema(many=True)
