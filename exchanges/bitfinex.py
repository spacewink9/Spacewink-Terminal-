import requests
import time
import hmac
import hashlib
import json

class Bitfinex:
    BASE_URL = "https://api.bitfinex.com/v1"

    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def _send_request(self, endpoint, params=None, method="GET"):
        nonce = str(int(time.time() * 10000000))
        if params:
            params["nonce"] = nonce
        else:
            params = {"nonce": nonce}

        url = self.BASE_URL + endpoint
        payload = json.dumps(params)
        signature = hmac.new(self.secret_key.encode(), payload.encode(), hashlib.sha384).hexdigest()
        headers = {
            "Content-Type": "application/json",
            "bfx-nonce": nonce,
            "bfx-apikey": self.api_key,
            "bfx-signature": signature
        }

        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=payload)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, params=params)

        if response.status_code != 200:
            raise Exception("Failed to send request: {}".format(response.text))

        return response.json()

    def get_ticker(self, symbol):
        endpoint = "/pubticker/{}".format(symbol)
        return self._send_request(endpoint)

    def get_order_book(self, symbol):
        endpoint = "/book/{}".format(symbol)
        return self._send_request(endpoint)

    def get_trade_history(self, symbol):
        endpoint = "/trades/{}".format(symbol)
        return self._send_request(endpoint)

    def place_order(self, symbol, amount, price, side, order_type, is_hidden=False):
        endpoint = "/order/new"
        params = {
            "symbol": symbol,
            "amount": str(amount),
            "price": str(price),
            "side": side,
            "type": order_type,
            "is_hidden": is_hidden
        }
        return self._send_request(endpoint, params, method="POST")

    def cancel_order(self, order_id):
        endpoint = "/order/cancel"
        params = {
            "order_id": order_id
        }
        return self._send_request(endpoint, params, method="POST")

    def get_order_status(self, order_id):
        endpoint = "/order/status"
        params = {
            "order_id": order_id
        }
        return self._send_request(endpoint, params)

    def get_account_balance(self):
        endpoint = "/balances"
        return self._send_request(endpoint)

    def get_order_history(self, symbol=None, limit=None):
        endpoint = "/mytrades"
        params = {}
        if symbol:
            params["symbol"] = symbol
        if limit:
            params["limit_trades"] = limit
        return self._send_request(endpoint, params)

    def get_open_orders(self, symbol=None):
        endpoint = "/orders"
        params = {}
        if symbol:
            params["symbol"] = symbol
        return self._send_request(endpoint, params)

