import requests
import hmac
import hashlib
import time

class Binance:
    def __init__(self, api_key, secret_key):
        self.API_KEY = api_key
        self.SECRET_KEY = secret_key
        self.BASE_URL = "https://api.binance.com"

    def _generate_signature(self, data):
        query_string = '&'.join([f"{k}={v}" for k,v in data.items()])
        return hmac.new(self.SECRET_KEY.encode(), query_string.encode(), hashlib.sha256).hexdigest()

    def _get_headers(self):
        return {
            "X-MBX-APIKEY": self.API_KEY
        }

    def _get(self, endpoint, data=None):
        url = f"{self.BASE_URL}{endpoint}"
        if data:
            signature = self._generate_signature(data)
            data['signature'] = signature
        response = requests.get(url, headers=self._get_headers(), params=data)
        return response.json()

    def get_ticker(self, symbol):
        endpoint = "/api/v3/ticker/price"
        data = {
            "symbol": symbol
        }
        return self._get(endpoint, data)

    def get_klines(self, symbol, interval):
        endpoint = "/api/v3/klines"
        data = {
            "symbol": symbol,
            "interval": interval
        }
        return self._get(endpoint, data)

    def place_limit_order(self, symbol, side, quantity, price):
        endpoint = "/api/v3/order"
        data = {
            "symbol": symbol,
            "side": side,
            "type": "LIMIT",
            "timeInForce": "GTC",
            "quantity": quantity,
            "price": price
        }
        return self._get(endpoint, data)
