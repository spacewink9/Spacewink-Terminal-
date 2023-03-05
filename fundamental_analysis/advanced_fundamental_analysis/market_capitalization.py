import pandas as pd

def calculate_market_capitalization(ticker: str, stock_price: float, number_of_shares: int) -> float:
    """
    Calculates the market capitalization for a given stock.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    stock_price (float): The current market price per share.
    number_of_shares (int): The total number of shares outstanding.

    Returns:
    float: The market capitalization.
    """
    # Calculate the market capitalization
    market_capitalization = stock_price * number_of_shares
    
    return market_capitalization
Market Capitalization = Stock Price * Number of Shares Outstanding
