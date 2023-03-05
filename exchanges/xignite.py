import requests
from market_data.market_data import MarketData


class Xignite(MarketData):
    """
    Xignite market data provider.
    """

    def __init__(self, api_key):
        self.base_url = "https://globalrealtime.xignite.com/v3"
        self.api_key = api_key

    def get_ticker_price(self, ticker):
        url = f"{self.base_url}/markets/realtime/prices/{ticker}.json"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
        }
        response = requests.get(url, headers=headers)
        response_json = response.json()
        last_price = response_json["lastSalePrice"]
        return float(last_price)
