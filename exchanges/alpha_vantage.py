import requests


class AlphaVantage:
    BASE_URL = "https://www.alphavantage.co/query"
    FUNCTION_MAPPING = {
        "daily": "TIME_SERIES_DAILY",
        "intraday": "TIME_SERIES_INTRADAY",
        "weekly": "TIME_SERIES_WEEKLY",
        "monthly": "TIME_SERIES_MONTHLY",
    }

    def __init__(self, api_key):
        self.api_key = api_key

    def get_data(self, symbol, function, **kwargs):
        function = self.FUNCTION_MAPPING.get(function, function)
        params = {
            "function": function,
            "symbol": symbol,
            "apikey": self.api_key,
            **kwargs,
        }
        response = requests.get(self.BASE_URL, params=params)
        if response.ok:
            return response.json()
        else:
            raise ValueError(f"Failed to fetch data for {symbol} from Alpha Vantage API: {response.content}")
