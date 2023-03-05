import numpy as np
import pandas as pd

def bbands(close_prices, window=20, num_std=2):
    """
    Calculate Bollinger Bands for given close prices using the specified window and number of standard deviations.
    
    Parameters:
    close_prices (numpy.ndarray or pandas.Series): Closing prices of the asset.
    window (int): Rolling window size to use for calculating the moving average and standard deviation.
    num_std (int): Number of standard deviations to use for the upper and lower bands.
    
    Returns:
    pandas.DataFrame: Dataframe containing the original prices along with the upper, middle, and lower bands.
    """
    # Calculate the rolling mean and standard deviation
    rolling_mean = close_prices.rolling(window=window).mean()
    rolling_std = close_prices.rolling(window=window).std()
    
    # Calculate the upper and lower bands
    upper_band = rolling_mean + num_std * rolling_std
    lower_band = rolling_mean - num_std * rolling_std
    
    # Combine everything into a single dataframe
    df = pd.DataFrame({'price': close_prices, 'upper_band': upper_band, 'middle_band': rolling_mean, 'lower_band': lower_band})
    
    return df
