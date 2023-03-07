import requests

class AlphaVantage:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://www.alphavantage.co/'

    def get_stock_price(self, symbol):
        url = f'{self.base_url}query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        return data['Global Quote']['05. price']

class NewsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://newsapi.org/v2/'

    def get_top_headlines(self, country):
        url = f'{self.base_url}top-headlines?country={country}&apiKey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        return data['articles']

class OpenWeatherMap:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.openweathermap.org/data/2.5/'

    def get_weather(self, city):
        url = f'{self.base_url}weather?q={city}&appid={self.api_key}'
        response = requests.get(url)
        data = response.json()
        return data['weather'][0]['description']

class PlaceholderAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = ''

    def get_data(self):
        # Placeholder API does not exist, returns sample data instead
        return {'data': 'This is sample data.'}
