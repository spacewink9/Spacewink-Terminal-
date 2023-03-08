from typing import Dict
import pandas as pd
import numpy as np
from strategy.base_strategy import BaseStrategy


class BreakoutStrategy(BaseStrategy):
    """
    A strategy that identifies breakouts from a given price range
    """

    def __init__(self, config: Dict):
        """
        Initializes the strategy with the given configuration
        """
        super().__init__(config)
        self.lookback_period = config.get('lookback_period', 20)
        self.breakout_percent = config.get('breakout_percent', 0.05)

    def backtest(self, prices: pd.DataFrame) -> pd.DataFrame:
        """
        Runs a backtest on the given prices and returns a DataFrame with the results
        """
        # Calculate the rolling high and low over the lookback period
        rolling_high = prices['close'].rolling(window=self.lookback_period).max()
        rolling_low = prices['close'].rolling(window=self.lookback_period).min()

        # Calculate the breakout threshold as a percentage of the rolling range
        rolling_range = rolling_high - rolling_low
        breakout_threshold = rolling_range * self.breakout_percent

        # Calculate the signals for entering and exiting trades
        long_signals = prices['close'] > rolling_high - breakout_threshold
        short_signals = prices['close'] < rolling_low + breakout_threshold

        # Combine the long and short signals to get the overall signal
        signals = long_signals.astype(int) - short_signals.astype(int)

        # Calculate the entry and exit prices based on the signals
        entry_prices = prices['open'].shift(1) * (1 + signals)
        exit_prices = prices['open'] * (1 - signals)

        # Calculate the profit and loss for each trade
        pl = exit_prices - entry_prices
        pl = pl.fillna(0)

        # Calculate the cumulative returns
        cumulative_returns = np.cumprod(1 + pl) - 1

        # Create a DataFrame with the results
        results = pd.DataFrame({
            'price': prices['close'],
            'signal': signals,
            'entry_price': entry_prices,
            'exit_price': exit_prices,
            'pl': pl,
            'cumulative_return': cumulative_returns
        })

        return results
