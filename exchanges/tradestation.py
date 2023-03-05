import requests
from exchanges.exchange import Exchange


class Tradestation(Exchange):
    def __init__(self, api_key: str, api_secret: str, api_version: str = 'v2'):
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_version = api_version
        self.base_url = f'https://api.tradestation.com/{self.api_version}'
    
    def get_markets(self):
        markets_url = f'{self.base_url}/markets'
        response = requests.get(markets_url)
        response.raise_for_status()
        return response.json()
    
    def get_ticker(self, symbol):
        ticker_url = f'{self.base_url}/quote/{symbol}'
        response = requests.get(ticker_url)
        response.raise_for_status()
        return response.json()
    
    def get_orderbook(self, symbol):
        orderbook_url = f'{self.base_url}/orderbook/{symbol}'
        response = requests.get(orderbook_url)
        response.raise_for_status()
        return response.json()
    
    def get_trades(self, symbol):
        trades_url = f'{self.base_url}/trades/{symbol}'
        response = requests.get(trades_url)
        response.raise_for_status()
        return response.json()
