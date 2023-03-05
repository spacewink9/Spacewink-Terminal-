import pandas as pd

def calculate_operating_margin(ticker: str, income_data: pd.DataFrame) -> float:
    """
    Calculates the operating margin for a given stock.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    income_data (pd.DataFrame): DataFrame containing the income statement data of the stock.

    Returns:
    float: The operating margin.
    """
    # Extract the relevant data from the income_data DataFrame
    operating_income = income_data.loc['Operating Income', :]
    total_revenue = income_data.loc['Total Revenue', :]
    
    # Calculate the operating margin
    operating_margin = operating_income / total_revenue
    
    return operating_margin
Operating Margin = Operating Income / Total Revenue
