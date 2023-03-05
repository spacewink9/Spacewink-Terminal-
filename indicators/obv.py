import numpy as np
import pandas as pd
from market_data import MarketData
from indicators import Indicator


class OBV(Indicator):
    def __init__(self, market_data: MarketData, window: int = 20):
        super().__init__(market_data)
        self.window = window

    def compute(self) -> pd.DataFrame:
        df = self.market_data.get_data()
        volume = df['Volume']
        close = df['Close']
        obv = np.where(close > close.shift(1), volume, np.where(close < close.shift(1), -volume, 0)).cumsum()
        obv_ma = obv.rolling(self.window).mean()
        return pd.DataFrame({'OBV': obv, 'OBV_MA': obv_ma})
