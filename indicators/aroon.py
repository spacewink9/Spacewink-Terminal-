import numpy as np
import pandas as pd

def aroon(df, period=25):
    high = df['high'].rolling(period, min_periods=period).apply(lambda x: x.argmax(), raw=True).fillna(0)
    low = df['low'].rolling(period, min_periods=period).apply(lambda x: x.argmin(), raw=True).fillna(0)
    aroon_up = ((period - high) / period) * 100
    aroon_down = ((period - low) / period) * 100
    return pd.DataFrame({'aroon_up': aroon_up, 'aroon_down': aroon_down})
