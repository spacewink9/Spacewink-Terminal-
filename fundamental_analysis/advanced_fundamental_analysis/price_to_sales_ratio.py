import pandas as pd

def calculate_price_to_sales_ratio(ticker: str, market_data: pd.DataFrame, income_data: pd.DataFrame) -> float:
    """
    Calculates the price-to-sales ratio for a given stock.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    market_data (pd.DataFrame): DataFrame containing the market data of the stock.
    income_data (pd.DataFrame): DataFrame containing the income statement data of the stock.

    Returns:
    float: The price-to-sales ratio.
    """
    # Extract the relevant data from the income_data DataFrame
    revenue = income_data.loc['Total Revenue', :]
    
    # Extract the relevant data from the market_data DataFrame
    shares_outstanding = market_data.loc['Shares Outstanding']
    current_price = market_data.loc['Current Price']
    
    # Calculate the price-to-sales ratio
    ps_ratio = current_price / (revenue / shares_outstanding)
    
    return ps_ratio
