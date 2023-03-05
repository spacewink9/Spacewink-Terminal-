import requests
import json
import time
from exchanges.base_exchange import BaseExchange

class Huobi(BaseExchange):
    def __init__(self):
        super().__init__()
        self.base_url = "https://api.huobi.pro"
        self.headers = {'Content-Type': 'application/json'}

    def get_symbols(self):
        url = self.base_url + "/v1/common/symbols"
        response = requests.get(url, headers=self.headers)
        symbols = []
        for symbol in response.json()["data"]:
            symbols.append(symbol["base-currency"] + symbol["quote-currency"])
        return symbols

    def get_ticker(self, symbol):
        url = self.base_url + "/market/detail/merged?symbol=" + symbol.lower()
        response = requests.get(url, headers=self.headers)
        ticker_data = response.json()["tick"]
        return {
            "symbol": symbol,
            "timestamp": ticker_data["ts"] / 1000,
            "last_price": ticker_data["close"],
            "volume": ticker_data["vol"],
            "high_price": ticker_data["high"],
            "low_price": ticker_data["low"],
            "bid": ticker_data["bid"][0],
            "ask": ticker_data["ask"][0]
        }

    def get_order_book(self, symbol, depth=20):
        url = self.base_url + "/market/depth?symbol=" + symbol.lower() + "&type=step0"
        response = requests.get(url, headers=self.headers)
        order_book_data = response.json()["tick"]
        bids = order_book_data["bids"][:depth]
        asks = order_book_data["asks"][:depth]
        bids = [[float(bid[0]), float(bid[1])] for bid in bids]
        asks = [[float(ask[0]), float(ask[1])] for ask in asks]
        return {"symbol": symbol, "bids": bids, "asks": asks}

    def get_recent_trades(self, symbol, limit=50):
        url = self.base_url + "/market/trade?symbol=" + symbol.lower()
        response = requests.get(url, headers=self.headers)
        trades_data = response.json()["data"][:limit]
        trades = []
        for trade_data in trades_data:
            trades.append({
                "timestamp": trade_data["ts"] / 1000,
                "symbol": symbol,
                "side": "buy" if trade_data["direction"] == "buy" else "sell",
                "price": trade_data["price"],
                "quantity": trade_data["amount"]
            })
        return trades

    def place_order(self, symbol, price, quantity, side, order_type):
        url = self.base_url + "/v1/order/orders/place"
        account_id = self.get_account_id()
        data = {
            "account-id": account_id,
            "symbol": symbol.lower(),
            "type": order_type,
            "amount": str(quantity),
            "price": str(price),
            "side": side
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(data))
        return response.json()["data"]

    def get_order_status(self, order_id):
        url = self.base_url + "/v1/order/orders/" + str(order_id)
        response = requests.get(url, headers=self.headers)
        return response.json()["data"]["state"]

    def cancel_order(self, order_id):
        url = self.base_url + "/v1/order/orders/" + str(order_id) + "/submitcancel"
        response = requests.post(url, headers=self.headers)
        return response.json()["data
