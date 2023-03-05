import alpha_vantage
from alpha_vantage.earnings import Earnings

# Set your API key here
API_KEY = 'YOUR_API_KEY'

# Create an instance of the Earnings class
earnings = Earnings(key=API_KEY, output_format='pandas')

# Retrieve historical earnings data for a specific stock
symbol = 'AAPL'
earnings_data, meta_data = earnings.get_earnings(symbol=symbol)

# Print the earnings data
print(earnings_data)
