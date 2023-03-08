import matplotlib.pyplot as plt
import mplfinance as mpf

def plot_ohlc(data, title='OHLC Chart', volume=True):
    """Plots OHLC chart using mplfinance library.
    
    Args:
    - data (pandas.DataFrame): Dataframe containing OHLCV data.
    - title (str): Title of the chart.
    - volume (bool): If True, also plots volume bars.
    """
    mpf.plot(data, type='candle', title=title, volume=volume, style='yahoo')
    plt.show()
