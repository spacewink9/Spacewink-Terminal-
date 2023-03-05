import requests
import pandas as pd

class Quandl:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.quandl.com/api/v3/"

    def get_stock_data(self, symbol, start_date, end_date):
        url = self.base_url + f"datasets/WIKI/{symbol}.json?start_date={start_date}&end_date={end_date}&api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        stock_data = pd.DataFrame(data["dataset"]["data"], columns=data["dataset"]["column_names"])
        return stock_data
