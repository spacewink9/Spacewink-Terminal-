import requests
import pandas as pd

def get_company_info(ticker: str) -> dict:
    """
    Retrieves information about a company given its ticker symbol.

    Parameters:
    ticker (str): Ticker symbol of the company.

    Returns:
    dict: A dictionary containing information about the company.
    """
    # Define the base URL for the API endpoint
    base_url = "https://financialmodelingprep.com/api/v3"

    # Define the endpoint for company profile information
    endpoint = f"{base_url}/profile/{ticker}"

    # Send a GET request to the API endpoint
    response = requests.get(endpoint)

    # Check if the request was successful
    if response.status_code != 200:
        raise ValueError(f"Failed to retrieve company info for {ticker}.")
    
    # Parse the response as JSON
    company_info = response.json()[0]

    # Create a dictionary of relevant company information
    company_dict = {
        "Company Name": company_info["companyName"],
        "Industry": company_info["industry"],
        "Sector": company_info["sector"],
        "Country": company_info["country"],
        "Market Cap": company_info["marketCap"],
        "Price": company_info["price"],
        "Beta": company_info["beta"],
        "PE Ratio": company_info["peRatio"],
        "Dividend Yield": company_info["lastDiv"],
        "Exchange": company_info["exchange"],
        "Currency": company_info["currency"],
        "Website": company_info["website"],
        "Description": company_info["description"],
    }

    return company_dict
