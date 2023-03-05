import requests

class Intrinio:

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api-v2.intrinio.com'

    def get_company_info(self, symbol):
        endpoint = f'{self.base_url}/companies/{symbol}'
        params = {'api_key': self.api_key}
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error getting company info for {symbol}: {response.content}')

    def get_stock_price(self, symbol):
        endpoint = f'{self.base_url}/securities/{symbol}/prices/latest'
        params = {'api_key': self.api_key}
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            json_data = response.json()
            return json_data['last_price']
        else:
            raise Exception(f'Error getting stock price for {symbol}: {response.content}')
