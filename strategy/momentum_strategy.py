import pandas as pd
from typing import Dict
from .base_strategy import BaseStrategy


class MomentumStrategy(BaseStrategy):
    def __init__(self):
        super().__init__()

    def set_config(self, config: Dict) -> None:
        self.config = config
        self.fast_window = config['fast_window']
        self.slow_window = config['slow_window']

    def run(self, data: pd.DataFrame) -> pd.DataFrame:
        # Calculate simple moving averages
        data[f'sma_{self.fast_window}'] = data['close'].rolling(self.fast_window).mean()
        data[f'sma_{self.slow_window}'] = data['close'].rolling(self.slow_window).mean()

        # Calculate the momentum
        data['momentum'] = data['close'] - data['close'].shift(self.fast_window)

        # Add a column to indicate whether the fast SMA is above the slow SMA
        data['sma_fast_above_slow'] = data[f'sma_{self.fast_window}'] > data[f'sma_{self.slow_window}']

        # Add a column to indicate whether the momentum is positive
        data['momentum_positive'] = data['momentum'] > 0

        # Add a column to indicate whether to buy or sell
        data['buy_signal'] = data['sma_fast_above_slow'] & data['momentum_positive']
        data['sell_signal'] = ~data['sma_fast_above_slow'] & data['momentum_positive']

        return data
