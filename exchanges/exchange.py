import requests
from typing import List


class Exchange:
    def __init__(self, name: str, base_url: str, api_key: str = None, secret_key: str = None):
        self.name = name
        self.base_url = base_url
        self.api_key = api_key
        self.secret_key = secret_key

    def get(self, endpoint: str, params: dict = None):
        url = self.base_url + endpoint
        headers = {}

        if self.api_key and self.secret_key:
            headers['API-Key'] = self.api_key
            headers['API-Sign'] = self._generate_signature(params)

        response = requests.get(url, headers=headers, params=params)

        return response.json()

    def post(self, endpoint: str, data: dict = None):
        url = self.base_url + endpoint
        headers = {}

        if self.api_key and self.secret_key:
            headers['API-Key'] = self.api_key
            headers['API-Sign'] = self._generate_signature(data)

        response = requests.post(url, headers=headers, json=data)

        return response.json()

    def _generate_signature(self, params: dict):
        return ''  # Replace with actual signature generation logic

    def get_supported_pairs(self) -> List[str]:
        raise NotImplementedError

    def get_ticker(self, symbol: str):
        raise NotImplementedError

    def get_orderbook(self, symbol: str, depth: int = 20):
        raise NotImplementedError

    def get_recent_trades(self, symbol: str):
        raise NotImplementedError

    def get_historical_trades(self, symbol: str, start_time: int, end_time: int):
        raise NotImplementedError

    def get_klines(self, symbol: str, interval: str, start_time: int, end_time: int):
        raise NotImplementedError

    def get_account_balances(self):
        raise NotImplementedError

    def get_order_history(self):
        raise NotImplementedError

    def create_limit_order(self, symbol: str, side: str, quantity: float, price: float):
        raise NotImplementedError

    def create_market_order(self, symbol: str, side: str, quantity: float):
        raise NotImplementedError

    def create_stop_order(self, symbol: str, side: str, quantity: float, price: float, stop_price: float):
        raise NotImplementedError
