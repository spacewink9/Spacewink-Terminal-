import pandas as pd

def calculate_gross_margin(ticker: str, income_data: pd.DataFrame) -> float:
    """
    Calculates the gross margin for a given stock.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    income_data (pd.DataFrame): DataFrame containing the income statement data of the stock.

    Returns:
    float: The gross margin.
    """
    # Extract the relevant data from the income_data DataFrame
    gross_profit = income_data.loc['Gross Profit', :]
    total_revenue = income_data.loc['Total Revenue', :]
    
    # Calculate the gross margin
    gross_margin = gross_profit / total_revenue
    
    return gross_margin
Gross Margin = Gross Profit / Total Revenue
