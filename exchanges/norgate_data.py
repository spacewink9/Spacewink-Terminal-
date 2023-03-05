import requests
import json
from datetime import datetime

class NorgateData:
    """
    Norgate Data API client for fetching historical data
    """

    API_URL = "https://api.norgatedata.com/api"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_history(self, symbol, start_date, end_date, interval="d1"):
        """
        Get historical data for a given symbol between a start and end date.
        Interval can be set to "d1" (daily), "w1" (weekly), "m1" (monthly).
        """
        url = f"{self.API_URL}/PriceHistory/{self.api_key}/{symbol}/{interval}/" \
              f"{datetime.strftime(start_date, '%Y-%m-%d')}/" \
              f"{datetime.strftime(end_date, '%Y-%m-%d')}/"

        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Error fetching data from Norgate Data API: {response.content}")

        data = json.loads(response.content)

        # parse data into OHLCV format
        ohlcv = []
        for record in data:
            timestamp = datetime.strptime(record["Date"], "%Y-%m-%dT%H:%M:%S")
            open_price = record["Open"]
            high_price = record["High"]
            low_price = record["Low"]
            close_price = record["Close"]
            volume = record["Volume"]

            ohlcv.append((timestamp, open_price, high_price, low_price, close_price, volume))

        return ohlcv
