import yfinance as yf
from datetime import datetime, timedelta

class DataDownloader:
    def __init__(self, start_date: str, end_date: str, symbols: list):
        self.start_date = start_date
        self.end_date = end_date
        self.symbols = symbols

    def download_data(self):
        prices = {}
        for symbol in self.symbols:
            print(f"Downloading {symbol} data...")
            ticker = yf.Ticker(symbol)
            data = ticker.history(start=self.start_date, end=self.end_date)
            prices[symbol] = data
        return prices
