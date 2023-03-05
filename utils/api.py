import requests

class API:
    def __init__(self, api_key=None):
        self.api_key = api_key
    
    def get_data(self, endpoint):
        url = f"https://{endpoint}"
        headers = {'Authorization': f'Bearer {self.api_key}'} if self.api_key else {}
        response = requests.get(url, headers=headers)
        return response.json()

class AlphaVantage(API):
    def __init__(self, api_key=None):
        super().__init__(api_key)
        self.endpoint = "www.alphavantage.co/query"
    
    def get_intraday_data(self, symbol, interval='1min'):
        query_params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": interval,
            "apikey": self.api_key
        }
        return self.get_data(f"{self.endpoint}", params=query_params)

class YahooFinance(API):
    def __init__(self, api_key=None):
        super().__init__(api_key)
        self.endpoint = "query1.finance.yahoo.com/v8/finance/chart"
    
    def get_historical_data(self, symbol, period1, period2):
        query_params = {
            "symbol": symbol,
            "period1": period1,
            "period2": period2,
            "interval": "1d",
            "events": "history",
            "crumb": "some_crumb",
        }
        return self.get_data(f"{self.endpoint}", params=query_params)

class Polygon(API):
    def __init__(self, api_key=None):
        super().__init__(api_key)
        self.endpoint = "api.polygon.io/v2/aggs/ticker"
    
    def get_aggregate_data(self, symbol, multiplier=1, timespan="day"):
        query_params = {
            "apiKey": self.api_key,
            "ticker": symbol,
            "multiplier": multiplier,
            "timespan": timespan,
            "from": "2018-03-01",
            "to": "2021-03-01"
        }
        return self.get_data(f"{self.endpoint}/{query_params['ticker']}/range/1/{query_params['timespan']}/{query_params['from']}/{query_params['to']}")
