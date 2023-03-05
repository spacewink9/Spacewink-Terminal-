import numpy as np
import pandas as pd
from market_data.bar import Bar
from indicators.init import Indicator

class ATR(Indicator):
    def __init__(self, window=14):
        super().__init__()
        self.window = window
        self.name = "ATR({})".format(window)

    def update(self, bar: Bar):
        self.add_bar(bar)

        if len(self.bars) < self.window + 1:
            return

        high_values = np.array([bar.high for bar in self.bars[-self.window:]])
        low_values = np.array([bar.low for bar in self.bars[-self.window:]])
        close_values = np.array([bar.close for bar in self.bars[-self.window-1:-1]])

        true_range = np.maximum(high_values - low_values, np.abs(high_values - close_values[:-1]))
        atr = pd.Series(true_range).rolling(window=self.window).mean().iloc[-1]

        self.value = atr
