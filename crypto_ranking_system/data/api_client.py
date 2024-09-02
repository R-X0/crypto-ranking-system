import requests
from config.settings import CMC_API_KEY, CMC_API_URL

class CoinMarketCapAPI:
    @staticmethod
    def fetch_latest_listings(limit=500):
        params = {
            'start': '1',
            'limit': str(limit),
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': CMC_API_KEY,
        }

        response = requests.get(CMC_API_URL, params=params, headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data['data']
        else:
            raise Exception(f"API request failed: {data['status']['error_message']}")