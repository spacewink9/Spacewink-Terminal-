import numpy as np
import pandas as pd

def cci(df, n, c=0.015):
    TP = (df['High'] + df['Low'] + df['Close']) / 3
    CCI = pd.Series((TP - TP.rolling(n).mean()) / (c * TP.rolling(n).std()), name='CCI')
    return df.join(CCI)
