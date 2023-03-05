import requests

# Replace YOUR_API_KEY with your actual API key from Finnhub
API_KEY = "YOUR_API_KEY"

def get_company_ratings(symbol):
    """
    Retrieves the ratings for the given company symbol using the Finnhub API.
    """
    url = f"https://finnhub.io/api/v1/stock/recommendation?symbol={symbol}&token={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if "error" in data:
        print(f"Error retrieving company ratings: {data['error']}")
        return None
    
    ratings = data["buy"] + data["hold"] + data["sell"]
    total = sum(ratings.values())
    
    return {
        "buy": ratings.get("buy", 0),
        "hold": ratings.get("hold", 0),
        "sell": ratings.get("sell", 0),
        "total": total
    }
