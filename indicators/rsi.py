import numpy as np
import pandas as pd

def rsi(close, period=14):
    """
    Calculates the Relative Strength Index (RSI) of a given closing price series.
    """
    delta = close.diff()

    # Get positive and negative gains
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # Calculate the moving average of gains and losses
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    # Calculate the RSI
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi
