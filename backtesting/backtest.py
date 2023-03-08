from typing import Dict, Any, Optional
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from .performance import Performance


class Backtest:
    def __init__(self, strategy, data: pd.DataFrame, initial_capital: float = 100000):
        self.strategy = strategy
        self.data = data
        self.initial_capital = initial_capital
        self.positions = pd.DataFrame(index=data.index).fillna(0.0)
        self.portfolio = pd.DataFrame(index=data.index).fillna(0.0)
        self.performance = Performance()

    def run_backtest(self) -> pd.DataFrame:
        self.strategy.set_data(self.data)
        self.strategy.set_initial_capital(self.initial_capital)

        signals = self.strategy.generate_signals()
        self.positions = self.generate_positions(signals)

        self.portfolio['holdings'] = (self.positions * self.data['close']).sum(axis=1)
        self.portfolio['cash'] = self.initial_capital - (self.positions.diff().fillna(0.0) * self.data['close']).sum(axis=1).cumsum()
        self.portfolio['total'] = self.portfolio['cash'] + self.portfolio['holdings']
        self.portfolio['returns'] = self.portfolio['total'].pct_change()
        self.performance.set_returns(self.portfolio['returns'])

        return self.portfolio

    def generate_positions(self, signals: pd.DataFrame) -> pd.DataFrame:
        positions = pd.DataFrame(index=signals.index).fillna(0.0)

        for symbol in signals.columns:
            # Buy signal
            positions[symbol][signals[symbol] == 1] = 1

            # Sell signal
            positions[symbol][signals[symbol] == -1] = 0

        # Ensure there are no naked positions
        positions.ffill(inplace=True)
        positions.fillna(0.0, inplace=True)

        return positions

    def plot(self):
        fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(15, 10))
        ax[0].plot(self.portfolio['total'], label='Total Portfolio Value')
        ax[0].plot(self.portfolio['holdings'], label='Holdings Value')
        ax[0].plot(self.portfolio['cash'], label='Cash')
        ax[0].legend()

        ax[1].plot(self.portfolio['returns'], label='Portfolio Returns')
        ax[1].plot(self.performance.get_rolling_mean(), label='Rolling Mean')
        ax[1].plot(self.performance.get_rolling_std(), label='Rolling Standard Deviation')
        ax[1].legend()

        plt.show()
