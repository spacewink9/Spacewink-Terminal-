import requests
import pandas as pd
from datetime import datetime, timedelta
from .base_exchange import BaseExchange


class Tiingo(BaseExchange):
    base_url = "https://api.tiingo.com"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_historical_data(self, symbol, start_date, end_date=None):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        else:
            end_date = datetime.today()

        url = f"{self.base_url}/tiingo/daily/{symbol}/prices"
        headers = {'Content-Type': 'application/json', 'Authorization': f'Token {self.api_key}'}
        params = {'startDate': start_date.strftime('%Y-%m-%d'), 'endDate': end_date.strftime('%Y-%m-%d')}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            raise ValueError(f"Error fetching data from Tiingo API: {response.content}")

        df = pd.read_json(response.content)
        df = df[['date', 'open', 'high', 'low', 'close', 'volume']]
        df['date'] = pd.to_datetime(df['date']).dt.date
        df.set_index('date', inplace=True)
        df.sort_index(inplace=True)

        return df

    def get_current_price(self, symbol):
        url = f"{self.base_url}/tiingo/daily/{symbol}/prices?startDate={datetime.now().strftime('%Y-%m-%d')}&resampleFreq=4min"
        headers = {'Content-Type': 'application/json', 'Authorization': f'Token {self.api_key}'}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise ValueError(f"Error fetching data from Tiingo API: {response.content}")

        data = response.json()
        if not data:
            raise ValueError(f"No data returned for symbol {symbol} from Tiingo API")

        last_price = data[-1]['close']
        return last_price
