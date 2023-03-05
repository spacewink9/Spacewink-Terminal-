from typing import Tuple, List
import pandas as pd
from indicators.sma import SMA

class MACD:
    def __init__(self, fast_period: int = 12, slow_period: int = 26, signal_period: int = 9):
        self.fast_period = fast_period
        self.slow_period = slow_period
        self.signal_period = signal_period

    def calculate(self, data: pd.DataFrame) -> Tuple[pd.Series, pd.Series]:
        ema_fast = data['close'].ewm(span=self.fast_period, adjust=False).mean()
        ema_slow = data['close'].ewm(span=self.slow_period, adjust=False).mean()
        macd_line = ema_fast - ema_slow
        signal_line = SMA(self.signal_period).calculate(macd_line)
        return macd_line, signal_line
