class PublisherGameStatsDTO:
    def __init__(self, publisher_id, publisher_name,
                 min_positive_rating, avg_positive_rating, max_positive_rating,
                 min_negative_rating, avg_negative_rating, max_negative_rating,
                 min_price, avg_price, max_price, game_count):
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name
        self.min_positive_rating = min_positive_rating
        self.avg_positive_rating = avg_positive_rating
        self.max_positive_rating = max_positive_rating
        self.min_negative_rating = min_negative_rating
        self.avg_negative_rating = avg_negative_rating
        self.max_negative_rating = max_negative_rating
        self.min_price = min_price
        self.avg_price = avg_price
        self.max_price = max_price
        self.game_count = game_count