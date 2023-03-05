import requests

API_KEY = 'your_api_key_here'
API_URL = f'https://api.news.com/market-news?apiKey={API_KEY}'

def get_market_news():
    """
    Fetches recent market news articles from a news API.
    
    Returns:
    A list of dictionaries, where each dictionary contains information about a market news article, including the title
    and a link to the full article.
    """
    response = requests.get(API_URL)
    if response.ok:
        data = response.json()
        articles = data['articles']
        market_news = []
        for article in articles:
            news_article = {
                'title': article['title'],
                'link': article['url']
            }
            market_news.append(news_article)
        return market_news
    else:
        raise ValueError(f'Error fetching market news: {response.text}')

if __name__ == '__main__':
    market_news = get_market_news()
    for article in market_news:
        print(f'{article["title"]}: {article["link"]}')
