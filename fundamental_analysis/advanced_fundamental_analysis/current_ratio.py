import pandas as pd

def calculate_current_ratio(ticker: str, balance_data: pd.DataFrame) -> float:
    """
    Calculates the current ratio for a given stock.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    balance_data (pd.DataFrame): DataFrame containing the balance sheet data of the stock.

    Returns:
    float: The current ratio.
    """
    # Extract the relevant data from the balance_data DataFrame
    current_assets = balance_data.loc['Current Assets', :]
    current_liabilities = balance_data.loc['Current Liabilities', :]
    
    # Calculate the current ratio
    current_ratio = current_assets / current_liabilities
    
    return current_ratio
