import requests
import json
from datetime import datetime
from prettytable import PrettyTable

class NewsAnalysis:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_company_news(self, symbol):
        """
        Fetches latest news for a given company symbol from News API
        """
        url = 'API_ADDRESS'
        params = {'q': symbol, 'apiKey': self.api_key}
        response = requests.get(url, params=params)
        news_data = json.loads(response.text)

        if news_data['status'] == 'ok':
            articles = news_data['articles']
            table = PrettyTable(['Title', 'Description', 'Source', 'Published At'])
            for article in articles:
                title = article['title']
                description = article['description']
                source = article['source']['name']
                published_at = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ').strftime('%m/%d/%Y %I:%M %p')
                table.add_row([title, description, source, published_at])
            print(table)
        else:
            print('Error occurred while fetching news!')

    def get_top_headlines(self):
        """
        Fetches top headlines from News API
        """
        url = 'API_ADDRESS'
        params = {'apiKey': self.api_key}
        response = requests.get(url, params=params)
        news_data = json.loads(response.text)

        if news_data['status'] == 'ok':
            articles = news_data['articles']
            table = PrettyTable(['Title', 'Description', 'Source', 'Published At'])
            for article in articles:
                title = article['title']
                description = article['description']
                source = article['source']['name']
                published_at = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ').strftime('%m/%d/%Y %I:%M %p')
                table.add_row([title, description, source, published_at])
            print(table)
        else:
            print('Error occurred while fetching news!')
