import pandas as pd
import numpy as np

def moving_average_strategy(dataframe, window_short=20, window_long=50):
    """
    Calculates moving averages for a given dataframe using short and long windows.
    Returns a signal to buy (1), sell (-1) or hold (0) for each data point based on whether
    the short moving average crosses above or below the long moving average.
    """
    signals = pd.DataFrame(index=dataframe.index)
    signals['signal'] = 0.0
    signals['short_ma'] = dataframe['close'].rolling(window=window_short, min_periods=1, center=False).mean()
    signals['long_ma'] = dataframe['close'].rolling(window=window_long, min_periods=1, center=False).mean()

    # Create a signal to buy when the short moving average crosses above the long moving average
    signals['signal'][window_long:] = np.where(signals['short_ma'][window_long:] > signals['long_ma'][window_long:], 1.0, 0.0)

    # Create a signal to sell when the short moving average crosses below the long moving average
    signals['signal'][window_long:] = np.where(signals['short_ma'][window_long:] < signals['long_ma'][window_long:], -1.0, signals['signal'][window_long:])

    return signals

def rsi_strategy(dataframe, window=14, oversold=30, overbought=70):
    """
    Calculates Relative Strength Index (RSI) for a given dataframe using a specified window.
    Returns a signal to buy (1), sell (-1) or hold (0) for each data point based on whether
    the RSI is oversold or overbought.
    """
    signals = pd.DataFrame(index=dataframe.index)
    signals['signal'] = 0.0
    delta = dataframe['close'].diff()

    # Get the gains and losses for each data point
    gains, losses = delta.copy(), delta.copy()
    gains[gains < 0] = 0
    losses[losses > 0] = 0

    # Calculate the average gains and losses over the specified window
    avg_gains = gains.rolling(window=window, min_periods=1).mean()
    avg_losses = losses.rolling(window=window, min_periods=1).mean().abs()

    # Calculate the Relative Strength
    rs = avg_gains / avg_losses

    # Calculate the RSI
    rsi = 100.0 - (100.0 / (1.0 + rs))

    # Create a signal to buy when the RSI is oversold
    signals['signal'] = np.where(rsi < oversold, 1.0, 0.0)

    # Create a signal to sell when the RSI is overbought
    signals['signal'] = np.where(rsi > overbought, -1.0, signals['signal'])

    return signals

def stochastic_strategy(dataframe, window=14, oversold=20, overbought=80):
    """
    Calculates Stochastic Oscillator for a given dataframe using a specified window.
    Returns a signal to buy (1), sell (-1) or hold (0) for each data point based on whether
    the Stochastic Oscillator is oversold or overbought.
    """
    signals = pd.DataFrame(index=dataframe.index)
    signals['signal'] = 0.0

    # Calculate the Stochastic Oscillator
    high = dataframe['high']
low = dataframe['low']
close = dataframe['close']
dataframe['stoch'] = ta.momentum.StochasticOscillator(high, low, close, window=14, smooth_window=3).stoch()

# Calculate the Moving Average Convergence Divergence (MACD)
dataframe['macd'], dataframe['macd_signal'], dataframe['macd_hist'] = ta.trend.MACD(close, window_slow=26, window_fast=12, window_signal=9)

# Calculate the Relative Strength Index (RSI)
dataframe['rsi'] = ta.momentum.RSIIndicator(close, window=14).rsi()

# Calculate the Bollinger Bands
dataframe['bb_upper'], dataframe['bb_middle'], dataframe['bb_lower'] = ta.volatility.BollingerBands(close, window=20, window_dev=2).bollinger_bands()

# Calculate the Average Directional Index (ADX)
dataframe['adx'] = ta.trend.ADXIndicator(high, low, close, window=14).adx()

# Calculate the Commodity Channel Index (CCI)
dataframe['cci'] = ta.trend.CCIIndicator(high, low, close, window=20).cci()

# Calculate the Chaikin Money Flow (CMF)
dataframe['cmf'] = ta.volume.ChaikinMoneyFlowIndicator(high, low, close, dataframe['volume'], window=20).chaikin_money_flow()

# Calculate the On-balance Volume (OBV)
dataframe['obv'] = ta.volume.OnBalanceVolumeIndicator(close, dataframe['volume']).on_balance_volume()

# Add a column to indicate whether the closing price is above the 20-day moving average
dataframe['above_20ma'] = close > ta.trend.SMAIndicator(close, window=20).sma_indicator()

# Add a column to indicate whether the closing price is above the 50-day moving average
dataframe['above_50ma'] = close > ta.trend.SMAIndicator(close, window=50).sma_indicator()

# Add a column to indicate whether the closing price is above the 200-day moving average
dataframe['above_200ma'] = close > ta.trend.SMAIndicator(close, window=200).sma_indicator()

# Add a column to indicate whether the MACD is bullish or bearish
dataframe['macd_bullish'] = (dataframe['macd'] > dataframe['macd_signal']) & (dataframe['macd_hist'] > 0)
dataframe['macd_bearish'] = (dataframe['macd'] < dataframe['macd_signal']) & (dataframe['macd_hist'] < 0)

return dataframe

