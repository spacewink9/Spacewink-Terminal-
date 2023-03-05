import numpy as np
import pandas as pd

def ichimoku(df, n1=9, n2=26, n3=52):
    """
    Function to calculate the Ichimoku Kinko Hyo indicator for a given DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing OHLCV data for a single trading pair.
    n1 (int): Number of periods to use for calculating the Conversion Line (default=9).
    n2 (int): Number of periods to use for calculating the Base Line (default=26).
    n3 (int): Number of periods to use for calculating the Leading Span B (default=52).

    Returns:
    pd.DataFrame: DataFrame containing the Ichimoku Kinko Hyo indicator values.
    """
    # Calculate the Conversion Line
    conv_line = (df['high'].rolling(n1).max() + df['low'].rolling(n1).min()) / 2

    # Calculate the Base Line
    base_line = (df['high'].rolling(n2).max() + df['low'].rolling(n2).min()) / 2

    # Calculate the Leading Span A
    span_a = (conv_line + base_line) / 2

    # Calculate the Leading Span B
    span_b = (df['high'].rolling(n3).max() + df['low'].rolling(n3).min()) / 2

    # Shift the Leading Span A and B forward
    span_a = span_a.shift(n2)
    span_b = span_b.shift(n2)

    # Create a DataFrame with the indicator values
    ichimoku_df = pd.DataFrame({
        'Conversion Line': conv_line,
        'Base Line': base_line,
        'Leading Span A': span_a,
        'Leading Span B': span_b,
        'Lagging Span': df['close'].shift(-n2)
    }, index=df.index)

    return ichimoku_df
