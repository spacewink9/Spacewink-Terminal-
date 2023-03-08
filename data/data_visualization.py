import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self, data):
        self.data = data
        
    def plot_line(self, x, y, title=None, xlabel=None, ylabel=None):
        plt.plot(x, y)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        plt.show()
        
    def plot_candlestick(self, data, title=None, xlabel=None, ylabel=None):
        fig, ax = plt.subplots()
        candlestick_ohlc(ax, data.values, width=0.6)
        ax.xaxis_date()
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        plt.show()
        
    def plot_histogram(self, data, title=None, xlabel=None, ylabel=None):
        sns.histplot(data)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        plt.show()
        
    def plot_scatter(self, x, y, title=None, xlabel=None, ylabel=None):
        plt.scatter(x, y)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        plt.show()

        
        import pandas as pd
from data_visualization import DataVisualizer

# Load data
data = pd.read_csv('data.csv')

# Create a DataVisualizer object
visualizer = DataVisualizer(data)

# Plot a line chart
visualizer.plot_line(data['date'], data['price'], title='Price over time', xlabel='Date', ylabel='Price')

# Plot a candlestick chart
visualizer.plot_candlestick(data[['date', 'open', 'high', 'low', 'close']], title='Candlestick chart')

# Plot a histogram
visualizer.plot_histogram(data['price'], title='Price distribution', xlabel='Price', ylabel='Count')

# Plot a scatter plot
visualizer.plot_scatter(data['volume'], data['price'], title='Volume vs. Price', xlabel='Volume', ylabel='Price')
