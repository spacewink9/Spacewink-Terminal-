import pandas as pd
from typing import Tuple
from .base_strategy import BaseStrategy


class MeanReversionStrategy(BaseStrategy):
    def __init__(self):
        super().__init__()
        self.mean_period = 20
        self.std_dev_factor = 2

    def set_config(self, config: dict) -> None:
        super().set_config(config)
        self.mean_period = config.get('mean_period', 20)
        self.std_dev_factor = config.get('std_dev_factor', 2)

    def backtest(self, prices: pd.DataFrame) -> Tuple[pd.DataFrame, float]:
        prices['mean'] = prices['close'].rolling(self.mean_period).mean()
        prices['std_dev'] = prices['close'].rolling(self.mean_period).std()
        prices['upper_band'] = prices['mean'] + self.std_dev_factor * prices['std_dev']
        prices['lower_band'] = prices['mean'] - self.std_dev_factor * prices['std_dev']
        prices['position'] = 0

        for i in range(1, len(prices)):
            if prices['close'][i] < prices['lower_band'][i-1]:
                prices['position'][i] = 1
            elif prices['close'][i] > prices['upper_band'][i-1]:
                prices['position'][i] = -1
            else:
                prices['position'][i] = prices['position'][i-1]

        prices['returns'] = prices['close'].pct_change() * prices['position'].shift(1)
        prices['strategy_returns'] = (prices['returns'] + 1).cumprod()

        return prices, prices['strategy_returns'][-1]
