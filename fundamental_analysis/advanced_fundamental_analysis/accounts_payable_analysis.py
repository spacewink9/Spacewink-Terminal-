import pandas as pd

def calculate_days_payable_outstanding(ticker: str, income_statement_data: pd.DataFrame, balance_sheet_data: pd.DataFrame) -> float:
    """
    Calculates the days payable outstanding for a given stock.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    income_statement_data (pd.DataFrame): DataFrame containing the income statement data of the stock.
    balance_sheet_data (pd.DataFrame): DataFrame containing the balance sheet data of the stock.

    Returns:
    float: The days payable outstanding.
    """
    # Extract the relevant data from the income_statement_data and balance_sheet_data DataFrames
    cost_of_goods_sold = income_statement_data.loc['Cost of Goods Sold', :]
    average_accounts_payable = (balance_sheet_data.loc['Accounts Payable', :-1] + balance_sheet_data.loc['Accounts Payable', 1:]) / 2
    
    # Calculate the days payable outstanding
    days_payable_outstanding = (average_accounts_payable / cost_of_goods_sold) * 365
    
    return days_payable_outstanding
Days Payable Outstanding = (Average Accounts Payable / Cost of Goods Sold) * 365
