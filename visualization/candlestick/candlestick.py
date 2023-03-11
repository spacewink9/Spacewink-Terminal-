import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
from mpl_finance import candlestick_ohlc
import pandas as pd

class CandlestickVisualizer:
    def __init__(self, data):
        self.data = data
        
    def plot(self):
        # Convert data to matplotlib-compatible format
        ohlc = self.data[['Date', 'Open', 'High', 'Low', 'Close']].copy()
        ohlc['Date'] = pd.to_datetime(ohlc['Date'])
        ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
        ohlc = ohlc.astype(float)
        ohlc = ohlc.values.tolist()
        
        # Create plot
        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.2)
        candlestick_ohlc(ax, ohlc, width=0.6, colorup='green', colordown='red')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Candlestick Chart')
        
        # Format x-axis ticks
        plt.xticks(rotation=45)
        ax.xaxis.set_major_locator(WeekdayLocator(MONDAY))
        ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
        ax.xaxis.set_minor_locator(DayLocator())
        
        # Show plot
        plt.show()
