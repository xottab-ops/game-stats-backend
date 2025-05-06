import pandas as pd
from app.extensions import db
from app.models import (
    Developer,
    Publisher,
    Game,
    Platform,
    PlatformGame,
    Category,
    CategoryGame,
)
from sqlalchemy.exc import ProgrammingError
import psycopg2


def load_data(csv_path):
    df = pd.read_csv(csv_path)

    # Преобразуем даты сразу для всего DataFrame
    df["release_date"] = pd.to_datetime(df["release_date"])

    # Кэш для уже обработанных записей
    developers_cache = {}
    publishers_cache = {}
    platforms_cache = {}
    categories_cache = {}

    for _, row in df.iterrows():
        try:
            developer_name = row["developer"]
            if developer_name not in developers_cache:
                developer = Developer.query.filter_by(name=developer_name).first()
                if not developer:
                    developer = Developer(name=developer_name)
                    db.session.add(developer)
                    db.session.flush()
                developers_cache[developer_name] = developer.id

            publisher_name = row["publisher"]
            if publisher_name not in publishers_cache:
                try:
                    publisher = Publisher.query.filter_by(name=publisher_name).first()
                    if not publisher:
                        publisher = Publisher(name=publisher_name)
                        db.session.add(publisher)
                        db.session.flush()
                    publishers_cache[publisher_name] = publisher.id
                except ProgrammingError as e:
                    if isinstance(e.orig, psycopg2.errors.UndefinedFunction):
                        print(
                            f"Пропускаем publisher с несовместимым типом: {publisher_name}"
                        )
                        publishers_cache[publisher_name] = None
                    else:
                        raise

            if publishers_cache.get(publisher_name) is None:
                continue

            game = Game(
                id=row["appid"],
                name=row["name"],
                release_date=row["release_date"],
                developer_id=developers_cache[developer_name],
                publisher_id=publishers_cache[publisher_name],
                positive_rating=row["positive_ratings"],
                negative_rating=row["negative_ratings"],
                price=row["price"],
            )
            db.session.add(game)
            db.session.flush()

            for platform_name in row["platforms"].split(";"):
                if platform_name not in platforms_cache:
                    platform = Platform.query.filter_by(name=platform_name).first()
                    if not platform:
                        platform = Platform(name=platform_name)
                        db.session.add(platform)
                        db.session.flush()
                    platforms_cache[platform_name] = platform.id

                db.session.add(
                    PlatformGame(
                        platform_id=platforms_cache[platform_name], game_id=game.id
                    )
                )

            for category_name in row["categories"].split(";"):
                if category_name not in categories_cache:
                    category = Category.query.filter_by(name=category_name).first()
                    if not category:
                        category = Category(name=category_name)
                        db.session.add(category)
                        db.session.flush()
                    categories_cache[category_name] = category.id

                db.session.add(
                    CategoryGame(
                        category_id=categories_cache[category_name], game_id=game.id
                    )
                )

            db.session.commit()

        except Exception as e:
            db.session.rollback()
            print(
                f"Ошибка при обработке игры {row['name']} (ID: {row['appid']}): {str(e)}"
            )
            continue
