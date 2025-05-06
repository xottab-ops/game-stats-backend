from app.extensions import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    games = db.relationship(
        "Game", secondary="category_game", back_populates="categories"
    )


class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    games = db.relationship(
        "Game", secondary="platform_game", back_populates="platforms"
    )


class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    games = db.relationship("Game", back_populates="developer")


class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    games = db.relationship("Game", back_populates="publisher")


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Date)
    developer_id = db.Column(db.Integer, db.ForeignKey("developer.id"))
    publisher_id = db.Column(db.Integer, db.ForeignKey("publisher.id"))
    positive_rating = db.Column(db.Integer, default=0)
    negative_rating = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, default=0.0)

    developer = db.relationship("Developer", back_populates="games")
    publisher = db.relationship("Publisher", back_populates="games")
    platforms = db.relationship(
        "Platform", secondary="platform_game", back_populates="games"
    )
    categories = db.relationship(
        "Category", secondary="category_game", back_populates="games"
    )


class PlatformGame(db.Model):
    platform_id = db.Column(db.Integer, db.ForeignKey("platform.id"), primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"), primary_key=True)


class CategoryGame(db.Model):
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"), primary_key=True)
