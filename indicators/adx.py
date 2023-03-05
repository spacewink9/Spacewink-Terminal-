import numpy as np
import pandas as pd

def adx(high: pd.Series, low: pd.Series, close: pd.Series, n: int = 14) -> pd.Series:
    """
    Calculates the Average Directional Index (ADX) indicator.
    :param high: High prices series.
    :param low: Low prices series.
    :param close: Close prices series.
    :param n: Window size.
    :return: A pandas Series with the ADX values.
    """
    # Calculate the true range.
    tr = pd.DataFrame(index=high.index)
    tr["hl"] = abs(high - low)
    tr["hc"] = abs(high - close.shift())
    tr["lc"] = abs(low - close.shift())
    tr["tr"] = tr[["hl", "hc", "lc"]].max(axis=1)
    
    # Calculate the positive directional movement (+DM) and negative directional movement (-DM).
    dm_pos = pd.Series(0, index=high.index)
    dm_neg = pd.Series(0, index=high.index)
    dm_pos[(high.diff() > 0) & (high.diff() > low.diff())] = high.diff()
    dm_neg[(low.diff() > 0) & (low.diff() > high.diff())] = low.diff()
    
    # Smooth the +DM and -DM series.
    di_pos = dm_pos.rolling(n).sum()
    di_neg = dm_neg.rolling(n).sum()
    
    # Calculate the directional movement index (DX) and the ADX.
    dx = 100 * (di_pos - di_neg).abs() / (di_pos + di_neg)
    adx = dx.rolling(n).mean()
    
    return adx
