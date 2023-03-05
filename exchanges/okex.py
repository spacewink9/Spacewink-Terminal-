import requests
from .exchange import Exchange


class OKEx(Exchange):
    def __init__(self, api_key: str, secret_key: str, passphrase: str):
        super().__init__(api_key, secret_key, passphrase)
        self.base_url = "https://www.okex.com/api/v5"

    def get_ticker(self, symbol: str):
        endpoint = f"{self.base_url}/market/ticker?instId={symbol}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            data = response.json()
            return {
                "symbol": symbol,
                "last_price": float(data["data"][0]["last"]),
                "bid_price": float(data["data"][0]["bidPx"]),
                "ask_price": float(data["data"][0]["askPx"]),
                "volume": float(data["data"][0]["vol"]),
            }
        else:
            return None

    def get_order_book(self, symbol: str, depth: int = 20):
        endpoint = f"{self.base_url}/market/books?instId={symbol}&sz={depth}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            data = response.json()
            bids = [[float(i["px"]), float(i["sz"])] for i in data["data"][0]["bids"]]
            asks = [[float(i["px"]), float(i["sz"])] for i in data["data"][0]["asks"]]
            return {
                "symbol": symbol,
                "bids": bids,
                "asks": asks,
            }
        else:
            return None

    def create_order(self, symbol: str, quantity: float, price: float, side: str, order_type: str = "limit"):
        endpoint = f"{self.base_url}/trade/order"
        if side.lower() == "buy":
            side = 1
        elif side.lower() == "sell":
            side = 2
        else:
            raise ValueError("Invalid order side. Must be 'buy' or 'sell'.")
        params = {
            "instId": symbol,
            "tdMode": "cash",
            "side": side,
            "ordType": order_type.upper(),
            "sz": quantity,
            "px": price,
        }
        response = requests.post(endpoint, json=params, headers=self.get_auth_headers())
        if response.status_code == 200:
            data = response.json()
            return {
                "symbol": symbol,
                "order_id": data["data"]["ordId"],
                "price": float(data["data"]["px"]),
                "quantity": float(data["data"]["sz"]),
                "side": side,
                "status": data["data"]["state"],
                "order_type": order_type.upper(),
            }
        else:
            return None

    def cancel_order(self, symbol: str, order_id: str):
        endpoint = f"{self.base_url}/trade/cancel-order"
        params = {
            "instId": symbol,
            "ordId": order_id,
        }
        response = requests.post(endpoint, json=params, headers=self.get_auth_headers())
        if response.status_code == 200:
            data = response.json()
            return {
                "symbol": symbol,
                "order_id": order_id,
                "status": data["data"]["state"],
            }
        else:
            return None
