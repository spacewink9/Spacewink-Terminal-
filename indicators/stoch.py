import numpy as np
import pandas as pd

def stochastic_oscillator(high, low, close, k_period=14, d_period=3, smoothing=1):
    """
    Calculates the Stochastic Oscillator for the given high, low, and close prices.

    Args:
        high (pd.Series): High prices for the asset.
        low (pd.Series): Low prices for the asset.
        close (pd.Series): Closing prices for the asset.
        k_period (int): Number of periods for the %K line. Default is 14.
        d_period (int): Number of periods for the %D line. Default is 3.
        smoothing (int): Smoothing factor for %D line. Default is 1.

    Returns:
        tuple: Returns a tuple containing two pd.Series: the %K line and the %D line.
    """

    # Calculate the lowest low and highest high for the given k_period
    low_min = low.rolling(window=k_period).min()
    high_max = high.rolling(window=k_period).max()

    # Calculate %K
    k = 100 * ((close - low_min) / (high_max - low_min))

    # Calculate %D
    d = k.rolling(window=d_period).mean().rolling(window=smoothing).mean()

    return k, d
