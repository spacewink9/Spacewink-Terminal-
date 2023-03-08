import pandas as pd
import numpy as np
import statsmodels.api as sm
from typing import List, Tuple
from .base_strategy import BaseStrategy


class PairsTradingStrategy(BaseStrategy):
    """
    Pairs Trading Strategy - long-short strategy that attempts to capture the price difference between two correlated
    assets by buying the underperforming asset and shorting the outperforming asset.

    Strategy:
    1. Identify a pair of assets that are highly correlated
    2. Calculate the spread between the two assets
    3. Buy the underperforming asset and short the outperforming asset when the spread is large
    4. Close the positions when the spread returns to its mean

    Parameters:
    - symbol_pairs: List of tuples containing the ticker symbols for the pair of assets to be traded
    - window_size: Lookback period for calculating z-score
    - z_score_threshold: Threshold for entering trades based on z-score
    - exit_z_score: Threshold for exiting trades based on z-score
    - exit_profit_pct: Profit target for closing trades
    - exit_loss_pct: Stop loss for closing trades
    """

    def __init__(self, symbol_pairs: List[Tuple[str, str]], window_size: int = 30, z_score_threshold: float = 2.0,
                 exit_z_score: float = 0.0, exit_profit_pct: float = 0.02, exit_loss_pct: float = 0.01):
        super().__init__()
        self.symbol_pairs = symbol_pairs
        self.window_size = window_size
        self.z_score_threshold = z_score_threshold
        self.exit_z_score = exit_z_score
        self.exit_profit_pct = exit_profit_pct
        self.exit_loss_pct = exit_loss_pct
        self.pair_ratios = {}

    def backtest(self, prices: pd.DataFrame) -> pd.DataFrame:
        """
        Backtests the pairs trading strategy on the given price data and returns a DataFrame with signals and P&L
        """
        pnl = pd.DataFrame()
        for symbol_pair in self.symbol_pairs:
            # Compute pair ratios
            pair_ratio = self.compute_pair_ratio(prices[symbol_pair[0]], prices[symbol_pair[1]])
            self.pair_ratios[symbol_pair] = pair_ratio

            # Compute z-scores
            z_score = self.compute_z_score(pair_ratio, self.window_size)

            # Compute signals
            signals = self.compute_signals(z_score)

            # Compute P&L
            pair_pnl = self.compute_pnl(signals, prices[symbol_pair[0]], prices[symbol_pair[1]])

            # Combine P&L with overall P&L
            pnl = pd.concat([pnl, pair_pnl], axis=1)

        # Combine P&L for all pairs
        pnl['total_pnl'] = pnl.sum(axis=1)

        # Add signals to prices DataFrame
        prices = pd.concat([prices, pnl[['signal']]], axis=1)

        return prices

    def compute_pair_ratio(self, x: pd.Series, y: pd.Series) -> pd.Series:
        """
        Computes the ratio between two assets in the given DataFrame
        """
        return x / y

    def compute_z_score(self, pair_ratio: pd.Series, window_size: int) -> pd.Series:
        """
        Computes the z-score of the pair ratio over the given window size
        """
        return (pair_ratio - pair_ratio.rolling(window_size).mean()) / pair_ratio.rolling(window_size).std()

    def compute_signals(self, z_score: pd.Series, spread: pd.Series) -> pd.Series:
    """
    Generate the trading signals based on the computed z-scores and spread values
    """

    # Initialize the trading signal series
    signals = pd.Series(index=z_score.index, dtype=int)

    # Set the threshold values for opening and closing a position
    # These values are based on the standard deviation of the spread
    # We use the mean and std values of the spread over the lookback period
    threshold_upper = self.mean_spread + self.std_spread * self.upper_threshold
    threshold_lower = self.mean_spread + self.std_spread * self.lower_threshold

    # Generate the trading signals
    # If the z-score exceeds the upper threshold, we open a short position on the ratio
    # If the z-score falls below the lower threshold, we open a long position on the ratio
    # If the z-score is between the two thresholds, we close any existing position
    signals[z_score > threshold_upper] = -1
    signals[z_score < threshold_lower] = 1
    signals[(z_score >= threshold_lower) & (z_score <= threshold_upper)] = 0

    # Apply the trading signal to the spread to generate the position series
    # If the signal is 1, we go long the spread (buy stock 1, sell stock 2)
    # If the signal is -1, we go short the spread (sell stock 1, buy stock 2)
    # If the signal is 0, we close any existing position
    positions = pd.Series(index=z_score.index, dtype=int)
    positions[signals == 1] = 1
    positions[signals == -1] = -1
    positions[signals == 0] = 0

    # Compute the daily returns of the spread and the position
    spread_returns = spread.pct_change()
    position_returns = spread_returns * positions.shift(1)

    # Compute the cumulative returns of the position
    cumulative_returns = position_returns.cumsum()

    # Return the trading signals, position, and cumulative returns
    return signals, positions, cumulative_returns

    
