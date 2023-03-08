import pandas as pd
import numpy as np
from typing import List, Dict
from datetime import datetime
from event import Event, SignalEvent
from strategy.base_strategy import BaseStrategy


class EventDrivenStrategy(BaseStrategy):
    def __init__(self, events: List[Event], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.events = events
        self.symbols = self.config['symbols']
        self.signals = pd.DataFrame(columns=self.symbols, index=['signal', 'entry_date'])
        self.holdings = pd.Series(index=self.symbols, dtype=np.int32)
        self.positions = pd.Series(index=self.symbols, dtype=np.int32)

    def set_config(self, config: Dict):
        super().set_config(config)
        self.events = self.config['events']

    def compute_signals(self, event: Event):
        if isinstance(event, SignalEvent) and event.symbol in self.symbols:
            self.signals[event.symbol]['signal'] = event.signal
            self.signals[event.symbol]['entry_date'] = event.datetime

    def backtest(self, prices: pd.DataFrame) -> pd.DataFrame:
        # Loop over the events
        for event in self.events:
            # Update signals based on events
            self.compute_signals(event)

            # Loop over the symbols
            for symbol in self.symbols:
                # Check if we have a signal for the symbol
                if self.signals[symbol]['signal'] is not None:
                    # Check if we have a position for the symbol
                    if self.positions[symbol] == 0:
                        # Enter a new position if we have a long signal
                        if self.signals[symbol]['signal'] == 1:
                            self.holdings[symbol] = 10000 / prices[symbol][event.datetime]
                            self.positions[symbol] = 1
                    # Exit the position if we have a short signal
                    elif self.signals[symbol]['signal'] == -1:
                        self.holdings[symbol] = 0
                        self.positions[symbol] = 0

        # Calculate the portfolio value
        portfolio_value = (self.holdings * prices).sum(axis=1)

        # Calculate the daily returns
        daily_returns = portfolio_value.pct_change()

        # Calculate the cumulative returns
        cumulative_returns = (1 + daily_returns).cumprod()

        # Create a DataFrame with the results
        results = pd.DataFrame({
            'portfolio_value': portfolio_value,
            'daily_returns': daily_returns,
            'cumulative_returns': cumulative_returns
        })

        return results
