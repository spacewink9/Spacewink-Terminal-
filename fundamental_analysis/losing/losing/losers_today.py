import requests
import json

url = "https://financialmodelingprep.com/api/v3/stock/losers"

response = requests.get(url)
data = json.loads(response.text)

print("Top 10 losers today:")
for i in range(10):
    print(f"{i+1}. {data[i]['symbol']}: {data[i]['changesPercentage']}")
