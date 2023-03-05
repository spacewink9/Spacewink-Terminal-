import requests

API_KEY = 'your_api_key_here'
COMPANY_NAME = 'Apple'  # Replace with the name of the company you want to search for
API_URL = f'https://api.news.com/company-news?q={COMPANY_NAME}&apiKey={API_KEY}'

def get_company_news():
    """
    Fetches recent news articles about a specific company from a news API.
    
    Returns:
    A list of dictionaries, where each dictionary contains information about a news article, including the title
    and a link to the full article.
    """
    response = requests.get(API_URL)
    if response.ok:
        data = response.json()
        articles = data['articles']
        company_news = []
        for article in articles:
            news_article = {
                'title': article['title'],
                'link': article['url']
            }
            company_news.append(news_article)
        return company_news
    else:
        raise ValueError(f'Error fetching company news: {response.text}')

if __name__ == '__main__':
    company_news = get_company_news()
    for article in company_news:
        print(f'{article["title"]}: {article["link"]}')
