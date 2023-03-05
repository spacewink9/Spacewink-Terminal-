import requests
import pandas as pd

def get_company_news(ticker: str) -> pd.DataFrame:
    """
    Retrieves the latest news articles related to a company given its ticker symbol.

    Parameters:
    ticker (str): Ticker symbol of the company.

    Returns:
    pd.DataFrame: A DataFrame containing the latest news articles related to the company.
    """
    # Define the base URL for the API endpoint
    base_url = "https://financialmodelingprep.com/api/v3"

    # Define the endpoint for company news articles
    endpoint = f"{base_url}/stock_news?tickers={ticker}&limit=10"

    # Send a GET request to the API endpoint
    response = requests.get(endpoint)

    # Check if the request was successful
    if response.status_code != 200:
        raise ValueError(f"Failed to retrieve news for {ticker}.")
    
    # Parse the response as JSON
    news_list = response.json()

    # Create a DataFrame of the news articles
    news_df = pd.DataFrame(news_list)

    # Extract relevant columns and rename them
    news_df = news_df[["publishedDate", "title", "image", "site"]]
    news_df = news_df.rename(columns={"publishedDate": "Published Date", "title": "Title", "image": "Image URL", "site": "Source"})

    return news_df
