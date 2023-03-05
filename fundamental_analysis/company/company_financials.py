import requests
import pandas as pd

def get_company_financials(ticker: str, statement_type: str = "income_statement", period: str = "annual") -> pd.DataFrame:
    """
    Retrieves the financial statements of a company given its ticker symbol, statement type, and period.

    Parameters:
    ticker (str): Ticker symbol of the company.
    statement_type (str): Type of financial statement to retrieve. Valid values are "income_statement",
        "balance_sheet_statement", and "cashflow_statement". Defaults to "income_statement".
    period (str): Time period for which to retrieve financial data. Valid values are "annual" and "quarter".
        Defaults to "annual".

    Returns:
    pd.DataFrame: A DataFrame containing the financial statements of the company.
    """
    # Define the base URL for the API endpoint
    base_url = "https://financialmodelingprep.com/api/v3"

    # Define the endpoint for company financials
    endpoint = f"{base_url}/{statement_type}/{ticker}?period={period}"

    # Send a GET request to the API endpoint
    response = requests.get(endpoint)

    # Check if the request was successful
    if response.status_code != 200:
        raise ValueError(f"Failed to retrieve financials for {ticker}.")

    # Parse the response as JSON
    data = response.json()

    # Create a DataFrame from the financial data
    df = pd.DataFrame(data)

    return df
