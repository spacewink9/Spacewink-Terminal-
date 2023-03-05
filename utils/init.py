import requests
import json

# Define the API key for accessing financial data
API_KEY = "your_api_key_here"

# Define the base URL for the financial data API
BASE_URL = "https://financial-data-api.com/api/v1/"

# Define a function to make API requests
def make_request(endpoint, params=None):
    """
    Makes a GET request to the financial data API.

    Parameters:
        - endpoint (str): the endpoint of the API to access
        - params (dict): a dictionary of query parameters

    Returns:
        - dict: the JSON response from the API
    """
    params = params or {}
    params["apikey"] = API_KEY

    url = BASE_URL + endpoint
    response = requests.get(url, params=params)
    response.raise_for_status()
    return json.loads(response.content)
