# price_to_book_ratio.py

import requests
import json

def get_price_to_book_ratio(ticker):
    """
    Get the price to book ratio for a given stock ticker.

    Args:
    ticker (str): Stock ticker symbol.

    Returns:
    float: The price to book ratio.
    """

    # Use Yahoo Finance API to get stock information
    url = f"https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}"
    response = requests.get(url)

    # Parse the HTML response using Beautiful Soup
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the price to book ratio using CSS selectors
    pb_ratio = soup.select("td[data-test='PB_RATIO-value']")[0].get_text()

    # Convert the string to a float and return the result
    return float(pb_ratio)

# Example usage
ticker = "AAPL"
pb_ratio = get_price_to_book_ratio(ticker)
print(f"The price to book ratio for {ticker} is {pb_ratio:.2f}")
