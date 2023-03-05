import requests
from exchanges.exchange import Exchange
from exchanges.market_data.bar import Bar
from exchanges.market_data.ticker import Ticker


class WorldTradingData(Exchange):
    def __init__(self, api_key):
        super().__init__()
        self.api_key = api_key
        self.base_url = "https://api.worldtradingdata.com/api/v1"

    def get_historical_data(self, symbol, interval="1", start_date=None, end_date=None):
        """
        Fetches historical price data for a given symbol and interval.
        :param symbol: The trading symbol to fetch data for (e.g. "AAPL").
        :param interval: The time interval for the price data (default is "1").
        :param start_date: The start date for the price data (default is None).
        :param end_date: The end date for the price data (default is None).
        :return: A list of Bar objects containing the historical price data.
        """
        params = {"symbol": symbol, "interval": interval, "api_token": self.api_key}
        if start_date:
            params["date_from"] = start_date
        if end_date:
            params["date_to"] = end_date
        response = requests.get(f"{self.base_url}/history", params=params)
        data = response.json()["history"]
        return [Bar(timestamp=key, open=value["open"], high=value["high"], low=value["low"], close=value["close"],
                    volume=value["volume"]) for key, value in data.items()]

    def get_ticker(self, symbol):
        """
        Fetches real-time ticker data for a given symbol.
        :param symbol: The trading symbol to fetch data for (e.g. "AAPL").
        :return: A Ticker object containing the real-time ticker data.
        """
        params = {"symbol": symbol, "api_token": self.api_key}
        response = requests.get(f"{self.base_url}/stock", params=params)
        data = response.json()["data"][0]
        return Ticker(symbol=symbol, bid=data["price"], ask=data["price"], last=data["price"], high=data["day_high"],
                      low=data["day_low"], volume=data["volume"], timestamp=data["last_trade_time"])
