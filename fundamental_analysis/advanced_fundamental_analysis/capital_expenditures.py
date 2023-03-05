import pandas as pd

def calculate_capital_expenditures(ticker: str, cash_flow_data: pd.DataFrame) -> float:
    """
    Calculates the capital expenditures for a given stock.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    cash_flow_data (pd.DataFrame): DataFrame containing the cash flow statement data of the stock.

    Returns:
    float: The capital expenditures.
    """
    # Extract the relevant data from the cash_flow_data DataFrame
    capital_expenditures = cash_flow_data.loc['Payments for Property, Plant and Equipment', :]
    
    return capital_expenditures
