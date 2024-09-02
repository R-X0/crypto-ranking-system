# services/data_processor.py
from data.database import Database

class DataProcessor:
    def __init__(self):
        self.db = Database()

    def process_and_store_data(self, coin_data):
        self.db.insert_coin_data(coin_data)

    def get_coin_ranking_trends(self, coin_symbol, days=7):
        return self.db.get_ranking_trends(coin_symbol, days)

    def close(self):
        self.db.close()