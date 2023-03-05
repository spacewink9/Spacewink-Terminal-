import pandas as pd

def calculate_days_sales_outstanding(ticker: str, income_statement_data: pd.DataFrame, balance_sheet_data: pd.DataFrame) -> float:
    """
    Calculates the days sales outstanding for a given stock.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    income_statement_data (pd.DataFrame): DataFrame containing the income statement data of the stock.
    balance_sheet_data (pd.DataFrame): DataFrame containing the balance sheet data of the stock.

    Returns:
    float: The days sales outstanding.
    """
    # Extract the relevant data from the income_statement_data and balance_sheet_data DataFrames
    sales = income_statement_data.loc['Total Revenue', :]
    average_accounts_receivable = (balance_sheet_data.loc['Accounts Receivable', :-1] + balance_sheet_data.loc['Accounts Receivable', 1:]) / 2
    
    # Calculate the days sales outstanding
    days_sales_outstanding = (average_accounts_receivable / sales) * 365
    
    return days_sales_outstanding
Days Sales Outstanding = (Average Accounts Receivable / Total Revenue) * 365
