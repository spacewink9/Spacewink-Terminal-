import requests
import pandas as pd

class EarningsHistory:
    def __init__(self, symbol):
        self.symbol = symbol
    
    def get_earnings_history(self):
        url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={self.symbol}&apikey=<YOUR_API_KEY>"
        res = requests.get(url)
        data = res.json()
        earnings_data = data["quarterlyEarnings"]
        earnings_df = pd.DataFrame(earnings_data)
        return earnings_df
