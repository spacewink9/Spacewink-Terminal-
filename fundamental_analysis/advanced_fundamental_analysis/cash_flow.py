import pandas as pd

def calculate_free_cash_flow(ticker: str, cash_flow_data: pd.DataFrame) -> float:
    """
    Calculates the free cash flow for a given stock.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    cash_flow_data (pd.DataFrame): DataFrame containing the cash flow statement data of the stock.

    Returns:
    float: The free cash flow.
    """
    # Extract the relevant data from the cash_flow_data DataFrame
    operating_cash_flow = cash_flow_data.loc['Net Cash provided by Operating Activities', :]
    capital_expenditures = cash_flow_data.loc['Payments for Property, Plant and Equipment', :]
    
    # Calculate the free cash flow
    free_cash_flow = operating_cash_flow - capital_expenditures
    
    return free_cash_flow
Free Cash Flow = Net Cash provided by Operating Activities - Payments for Property, Plant and Equipment
