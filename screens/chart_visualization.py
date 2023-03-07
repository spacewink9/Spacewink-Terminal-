import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

def get_stock_data(symbol, start_date, end_date):
    """
    Fetches stock data from Yahoo Finance API
    """
    stock_data = pdr.get_data_yahoo(symbol, start=start_date, end=end_date)
    return stock_data

def plot_stock_data(stock_data, title):
    """
    Plots stock data using Matplotlib
    """
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data["Adj Close"])
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.show()

def chart_visualization():
    """
    Main function for chart visualization screen
    """
    print("Welcome to Chart Visualization")

    # Get input parameters
    symbol = input("Enter stock symbol (e.g. AAPL): ")
    start_date = input("Enter start date (yyyy-mm-dd): ")
    end_date = input("Enter end date (yyyy-mm-dd): ")
    title = input("Enter chart title: ")

    # Fetch and plot stock data
    stock_data = get_stock_data(symbol, start_date, end_date)
    plot_stock_data(stock_data, title)

    print("Thank you for using Chart Visualization")
