import requests
import time
from .exchange import Exchange
from ..utils.exceptions import *
from ..utils.utils import format_pair


class IEXCloud(Exchange):
    API_URL = 'https://cloud.iexapis.com/'

    def __init__(self, api_key):
        self.api_key = api_key
        super().__init__()

    def get_symbols(self):
        url = self.API_URL + 'stable/ref-data/symbols?token=' + self.api_key
        response = requests.get(url)

        if response.status_code != 200:
            raise ExchangeError('Unable to retrieve symbols')

        symbols = []
        for symbol in response.json():
            symbols.append(symbol['symbol'])

        return symbols

    def get_price(self, pair):
        symbol = format_pair(pair, self.SEPARATOR)
        url = self.API_URL + f'stable/stock/{symbol}/quote?token={self.api_key}'
        response = requests.get(url)

        if response.status_code != 200:
            raise ExchangeError(f'Unable to retrieve price for {pair}')

        return response.json()['latestPrice']

    def get_order_book(self, pair, depth=100):
        raise NotImplementedError('IEX Cloud does not support order book retrieval')

    def get_trade_history(self, pair, start_time=None, end_time=None):
        symbol = format_pair(pair, self.SEPARATOR)
        if start_time is None:
            start_time = int(time.time()) - 24 * 60 * 60  # last 24 hours
        if end_time is None:
            end_time = int(time.time())
        start_time = int(start_time * 1000)
        end_time = int(end_time * 1000)

        url = self.API_URL + f'stable/stock/{symbol}/trades/last?token={self.api_key}&format=csv&filter='\
              f'time,price,size&from={start_time}&to={end_time}'
        response = requests.get(url)

        if response.status_code != 200:
            raise ExchangeError(f'Unable to retrieve trade history for {pair}')

        trades = []
        for trade in response.text.splitlines()[1:]:
            trade_data = trade.split(',')
            trades.append({
                'time': int(trade_data[0]) // 1000,
                'price': float(trade_data[1]),
                'amount': float(trade_data[2])
            })

        return trades
