import pandas as pd
import numpy as np
from ta import add_all_ta_features

def generate_features(df):
    """
    Generates additional features for a given DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with OHLCV data

    Returns
    -------
    pd.DataFrame
        DataFrame with additional features added
    """
    # Add technical analysis features using TA-Lib
    # and Technical Analysis Library (ta)
    ta_features = add_all_ta_features(df, open="Open", high="High", low="Low", close="Close", volume="Volume")

    # Add custom features
    # For example, you could calculate the Bollinger Band width and add it as a feature
    std_dev = df['Close'].rolling(window=20).std()
    ma = df['Close'].rolling(window=20).mean()
    upper_band = ma + 2 * std_dev
    lower_band = ma - 2 * std_dev
    bb_width = (upper_band - lower_band) / ma
    ta_features['bb_width'] = bb_width

    # Return DataFrame with added features
    return ta_features

def split_data(df, split_ratio=0.8):
    """
    Splits a DataFrame into train and test sets.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with OHLCV data
    split_ratio : float
        Ratio of data to use for training (default is 0.8)

    Returns
    -------
    tuple of pd.DataFrames
        A tuple of train and test DataFrames
    """
    split_index = int(len(df) * split_ratio)
    train_data = df.iloc[:split_index]
    test_data = df.iloc[split_index:]
    return train_data, test_data

def normalize_data(df):
    """
    Normalizes a DataFrame using min-max scaling.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with OHLCV data

    Returns
    -------
    pd.DataFrame
        Normalized DataFrame
    """
    # Apply min-max scaling to all columns except the date column
    for col in df.columns[1:]:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df
