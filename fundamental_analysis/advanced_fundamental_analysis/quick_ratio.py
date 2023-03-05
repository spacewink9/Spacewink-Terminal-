import pandas as pd

def calculate_quick_ratio(ticker: str, balance_data: pd.DataFrame) -> float:
    """
    Calculates the quick ratio for a given stock.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    balance_data (pd.DataFrame): DataFrame containing the balance sheet data of the stock.

    Returns:
    float: The quick ratio.
    """
    # Extract the relevant data from the balance_data DataFrame
    current_assets = balance_data.loc['Current Assets', :]
    current_liabilities = balance_data.loc['Current Liabilities', :]
    inventory = balance_data.loc['Inventory', :]
    
    # Calculate the quick ratio
    quick_ratio = (current_assets - inventory) / current_liabilities
    
    return quick_ratio
