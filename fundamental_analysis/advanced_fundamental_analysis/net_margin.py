import pandas as pd

def calculate_net_margin(ticker: str, income_data: pd.DataFrame) -> float:
    """
    Calculates the net margin for a given stock.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    income_data (pd.DataFrame): DataFrame containing the income statement data of the stock.

    Returns:
    float: The net margin.
    """
    # Extract the relevant data from the income_data DataFrame
    net_income = income_data.loc['Net Income', :]
    total_revenue = income_data.loc['Total Revenue', :]
    
    # Calculate the net margin
    net_margin = net_income / total_revenue
    
    return net_margin
Net Margin = Net Income / Total Revenue
