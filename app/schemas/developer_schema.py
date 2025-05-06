from marshmallow import Schema, fields


class DeveloperGameStatsSchema(Schema):
    developer_id = fields.Int()
    developer_name = fields.Str()

    min_positive_rating = fields.Int()
    avg_positive_rating = fields.Float()
    max_positive_rating = fields.Int()

    min_negative_rating = fields.Int()
    avg_negative_rating = fields.Float()
    max_negative_rating = fields.Int()

    min_price = fields.Float()
    avg_price = fields.Float()
    max_price = fields.Float()

    game_count = fields.Int()


developer_schema = DeveloperGameStatsSchema(many=True)
