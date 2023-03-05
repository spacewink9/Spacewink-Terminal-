import numpy as np
from .utils import get_candle_data

def ema(data, period):
    close_prices = get_candle_data(data, 'close')
    ema_values = np.zeros(len(close_prices))
    ema_values[0] = close_prices[0]
    multiplier = 2 / (period + 1)
    for i in range(1, len(close_prices)):
        ema_values[i] = (close_prices[i] - ema_values[i - 1]) * multiplier + ema_values[i - 1]
    return ema_values
