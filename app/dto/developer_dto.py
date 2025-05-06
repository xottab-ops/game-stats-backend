class DeveloperGameStatsDTO:
    def __init__(
        self,
        developer_id,
        developer_name,
        min_positive_rating,
        avg_positive_rating,
        max_positive_rating,
        min_negative_rating,
        avg_negative_rating,
        max_negative_rating,
        min_price,
        avg_price,
        max_price,
        game_count,
    ):
        self.developer_id = developer_id
        self.developer_name = developer_name
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
