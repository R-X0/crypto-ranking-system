# services/data_fetcher.py
from data.api_client import CoinMarketCapAPI
from models.coin import Coin

class DataFetcher:
    @staticmethod
    def fetch_latest_coin_data():
        raw_data = CoinMarketCapAPI.fetch_latest_listings()
        return [
            Coin(
                coin_id=coin['id'],
                name=coin['name'],
                symbol=coin['symbol'],
                rank=coin['cmc_rank'],
                price=coin['quote']['USD']['price'],
                market_cap=coin['quote']['USD']['market_cap'],
                volume_24h=coin['quote']['USD']['volume_24h']
            )
            for coin in raw_data
        ]