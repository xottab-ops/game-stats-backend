import pandas as pd
from app.extensions import db
from app.models import Developer, Publisher, Game, Platform, PlatformGame, Category, CategoryGame

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        developer = Developer.query.filter_by(name=row["developer"]).first()
        if not developer:
            developer = Developer(name=row["developer"])
            db.session.add(developer)
            db.session.commit()

        publisher = Publisher.query.filter_by(name=row["publisher"]).first()
        if not publisher:
            publisher = Publisher(name=row["publisher"])
            db.session.add(publisher)
            db.session.commit()

        game = Game(
            id=row["appid"],
            name=row["name"],
            release_date=pd.to_datetime(row["release_date"]),
            developer_id=developer.id,
            publisher_id=publisher.id,
            positive_rating=row["positive_ratings"],
            negative_rating=row["negative_ratings"],
            price=row["price"],
        )
        db.session.add(game)
        db.session.commit()

        for platform_name in row["platforms"].split(";"):
            platform = Platform.query.filter_by(name=platform_name).first()
            if not platform:
                platform = Platform(name=platform_name)
                db.session.add(platform)
                db.session.commit()
            db.session.add(PlatformGame(platform_id=platform.id, game_id=game.id))

        for category_name in row["categories"].split(";"):
            category = Category.query.filter_by(name=category_name).first()
            if not category:
                category = Category(name=category_name)
                db.session.add(category)
                db.session.commit()
            db.session.add(CategoryGame(category_id=category.id, game_id=game.id))

        db.session.commit()
