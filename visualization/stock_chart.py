import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
import pandas as pd


class StockChart:
    def __init__(self, data):
        self.data = data

    def plot(self, title=None, xlabel='Date', ylabel='Price', figsize=(10, 5)):
        fig, ax = plt.subplots(figsize=figsize)
        
        # Set title
        if title:
            ax.set_title(title)
        
        # Set x-axis and y-axis labels
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        
        # Set x-axis date formatting
        weeks = WeekdayLocator(MONDAY)
        days = DayLocator()
        days_format = DateFormatter('%d')
        
        ax.xaxis.set_major_locator(weeks)
        ax.xaxis.set_minor_locator(days)
        ax.xaxis.set_major_formatter(days_format)
        
        # Plot data
        ax.plot(self.data['date'], self.data['close'])
        
        # Show grid
        ax.grid(True)
        
        # Show plot
        plt.show()
