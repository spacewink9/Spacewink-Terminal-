import requests
import time
import hmac
import hashlib
from urllib.parse import urljoin

from .exchange import Exchange

class FTX(Exchange):
"""
FTX API
"""
def __init__(self, api_key, api_secret, subaccount=None):
    super().__init__(api_key, api_secret, subaccount)

    self.base_url = 'https://ftx.com/api/'
    self.headers = {
        'FTX-KEY': self.api_key,
        'FTX-SIGN': '',
        'FTX-TS': '',
        'FTX-SUBACCOUNT': self.subaccount,
    }

def _generate_signature(self, endpoint, method, timestamp, data=''):
    message = f'{timestamp}{method}{urljoin(self.base_url, endpoint)}{data}'
    signature = hmac.new(self.api_secret.encode(), message.encode(), hashlib.sha256).hexdigest()
    self.headers['FTX-SIGN'] = signature
    self.headers['FTX-TS'] = str(timestamp)

def _make_request(self, endpoint, method, params=None, data=None):
    url = urljoin(self.base_url, endpoint)

    timestamp = int(time.time() * 1000)
    self._generate_signature(endpoint, method.upper(), timestamp, data=data)

    response = requests.request(method, url, headers=self.headers, params=params, data=data)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Request failed with status {response.status_code}: {response.text}')

def get_balance(self, coin):
    endpoint = 'wallet/balances'
    response = self._make_request(endpoint, 'GET')

    for balance in response:
        if balance['coin'] == coin:
            return float(balance['free'])

    raise Exception(f'Failed to find {coin} balance')

def get_ticker(self, market):
    endpoint = f'markets/{market}'
    response = self._make_request(endpoint, 'GET')

    return response['result']

def get_orderbook(self, market, depth=20):
    endpoint = f'markets/{market}/orderbook'
    params = {
        'depth': depth,
    }
    response = self._make_request(endpoint, 'GET', params=params)

    return response['result']

def place_limit_order(self, market, side, price, size):
    endpoint = 'orders'
    data = {
        'market': market,
        'side': side.upper(),
        'price': price,
        'size': size,
        'type': 'limit',
        'postOnly': True,
    }
    response = self._make_request(endpoint, 'POST', data=data)

    return response['result']

def place_market_order(self, market, side, size):
    endpoint = 'orders'
    data = {
        'market': market,
        'side': side.upper(),
        'size': size,
        'type': 'market',
    }
    response = self._make_request(endpoint, 'POST', data=data)

    return response['result']

def get_order(self, order_id):
    endpoint = f'orders/{order_id}'
    response = self._make_request(endpoint, 'GET')

    return response['result']

def cancel_order(self, order_id):
    endpoint = f'orders/{
