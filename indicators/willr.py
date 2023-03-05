import numpy as np
from indicators.sma import sma

def willr(high, low, close, timeperiod=14):
    """
    Calculate the Williams %R indicator for the given data.

    Parameters:
    high (list): A list of high prices.
    low (list): A list of low prices.
    close (list): A list of closing prices.
    timeperiod (int): The time period to use for the calculation. Default is 14.

    Returns:
    list: A list of Williams %R values for each corresponding period.
    """
    highest_high = np.max(high[:timeperiod])
    lowest_low = np.min(low[:timeperiod])

    wr = []
    for i in range(timeperiod, len(close)):
        hh = np.max(high[i - timeperiod:i])
        ll = np.min(low[i - timeperiod:i])
        wr_value = ((hh - close[i]) / (hh - ll)) * -100
        wr.append(wr_value)

    return wr
