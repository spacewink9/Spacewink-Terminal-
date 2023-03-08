from typing import List
import pandas as pd
from datetime import datetime, timedelta
from .backtest import Backtest
from .backtest_result import BacktestResult
from ..strategy.base_strategy import BaseStrategy


class Backtester:
    def __init__(self, strategy: BaseStrategy, start_date: datetime, end_date: datetime, initial_capital: float = 100000):
        self.strategy = strategy
        self.start_date = start_date
        self.end_date = end_date
        self.initial_capital = initial_capital

    def backtest(self) -> BacktestResult:
        prices = self._get_historical_prices()
        backtest = Backtest(self.strategy, prices, self.initial_capital)
        result = backtest.run()
        return result

    def optimize(self, param_ranges: dict) -> BacktestResult:
        prices = self._get_historical_prices()
        backtest = Backtest(self.strategy, prices, self.initial_capital)
        result = backtest.optimize(param_ranges)
        return result

    def _get_historical_prices(self) -> pd.DataFrame:
        start_date_str = self.start_date.strftime("%Y-%m-%d")
        end_date_str = self.end_date.strftime("%Y-%m-%d")

        prices = pd.DataFrame()
        for symbol in self.strategy.symbols:
            df = pd.read_csv(f"data/{symbol}.csv", index_col="date", parse_dates=["date"])
            df = df.loc[start_date_str:end_date_str]
            df["symbol"] = symbol
            prices = pd.concat([prices, df])

        prices.reset_index(inplace=True)
        prices.drop_duplicates(subset=["symbol", "date"], inplace=True)
        prices.set_index(["symbol", "date"], inplace=True)
        prices.sort_index(inplace=True)
        return prices
