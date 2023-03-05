import pandas as pd

def calculate_return_on_equity(ticker: str, income_statement_data: pd.DataFrame, balance_sheet_data: pd.DataFrame) -> float:
    """
    Calculates the return on equity for a given stock.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    income_statement_data (pd.DataFrame): DataFrame containing the income statement data of the stock.
    balance_sheet_data (pd.DataFrame): DataFrame containing the balance sheet data of the stock.

    Returns:
    float: The return on equity.
    """
    # Extract the relevant data from the income_statement_data and balance_sheet_data DataFrames
    net_income = income_statement_data.loc['Net Income', :]
    average_shareholder_equity = (balance_sheet_data.loc['Total Stockholders\' Equity', :-1] + balance_sheet_data.loc['Total Stockholders\' Equity', 1:]) / 2
    
    # Calculate the return on equity
    return_on_equity = (net_income / average_shareholder_equity) * 100
    
    return return_on_equity
Return on Equity = (Net Income / Average Shareholder Equity) * 100
