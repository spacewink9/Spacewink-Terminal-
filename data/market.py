import pandas as pd
from typing import List

class Market:
    def __init__(self, symbols: List[str], start_date: str, end_date: str):
        self.symbols = symbols
        self.start_date = start_date
        self.end_date = end_date
        self.prices = self._load_prices()

    def _load_prices(self) -> pd.DataFrame:
        prices = pd.DataFrame()
        for symbol in self.symbols:
            file_path = f"data/{symbol}.csv"
            df = pd.read_csv(file_path, index_col="date", parse_dates=True,
                             usecols=["date", "close"], na_values=["nan"])
            df = df.loc[self.start_date:self.end_date]
            df.rename(columns={"close": symbol}, inplace=True)
            prices = prices.join(df, how="outer")
        return prices.dropna()

    def get_price(self, symbol: str, date: str) -> float:
        return self.prices.loc[date, symbol]

    def update_prices(self, symbol: str, new_prices: pd.DataFrame):
        # update csv or database entry with new prices
        self.prices[symbol] = new_prices

    def get_symbols(self) -> List[str]:
        return self.symbols

    def get_start_date(self) -> str:
        return self.start_date

    def get_end_date(self) -> str:
        return self.end_date

    def get_prices(self) -> pd.DataFrame:
        return self.prices
