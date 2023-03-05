import pandas as pd

def calculate_inventory_turnover_ratio(ticker: str, income_statement_data: pd.DataFrame, balance_sheet_data: pd.DataFrame) -> float:
    """
    Calculates the inventory turnover ratio for a given stock.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    income_statement_data (pd.DataFrame): DataFrame containing the income statement data of the stock.
    balance_sheet_data (pd.DataFrame): DataFrame containing the balance sheet data of the stock.

    Returns:
    float: The inventory turnover ratio.
    """
    # Extract the relevant data from the income_statement_data and balance_sheet_data DataFrames
    cost_of_goods_sold = income_statement_data.loc['Cost of Goods Sold', :]
    average_inventory = (balance_sheet_data.loc['Inventory', :-1] + balance_sheet_data.loc['Inventory', 1:]) / 2
    
    # Calculate the inventory turnover ratio
    inventory_turnover_ratio = cost_of_goods_sold / average_inventory
    
    return inventory_turnover_ratio
Inventory Turnover Ratio = Cost of Goods Sold / Average Inventory
