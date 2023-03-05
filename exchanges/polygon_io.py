import requests
from .exchange import Exchange


class PolygonIO(Exchange):
    def __init__(self, api_key):
        super().__init__()
        self.api_key = api_key
        self.base_url = 'https://api.polygon.io/'

    def get_exchange_name(self):
        return 'PolygonIO'

    def get_supported_pairs(self):
        return ['BTC-USD', 'ETH-USD', 'ADA-USD']

    def get_current_price(self, pair):
        url = f'{self.base_url}/v1/last/crypto/{pair}?apiKey={self.api_key}'
        response = requests.get(url).json()
        return float(response['last'])

    def get_historical_prices(self, pair, start_date, end_date):
        url = f'{self.base_url}/v2/aggs/ticker/crypto/{pair}/range/1/day/{start_date}/{end_date}?apiKey={self.api_key}'
        response = requests.get(url).json()
        prices = []
        for result in response['results']:
            prices.append({
                'date': result['t'],
                'open': result['o'],
                'high': result['h'],
                'low': result['l'],
                'close': result['c'],
                'volume': result['v']
            })
        return prices
