import requests

API_KEY = 'your_api_key_here'
API_URL = f'https://api.news.com/top-headlines?country=us&category=business&apiKey={API_KEY}'

def get_top_headlines():
    """
    Fetches top business headlines from a news API.
    
    Returns:
    A list of dictionaries, where each dictionary contains information about a top business headline, including the title
    and a link to the full article.
    """
    response = requests.get(API_URL)
    if response.ok:
        data = response.json()
        articles = data['articles']
        headlines = []
        for article in articles:
            headline = {
                'title': article['title'],
                'link': article['url']
            }
            headlines.append(headline)
        return headlines
    else:
        raise ValueError(f'Error fetching top headlines: {response.text}')

if __name__ == '__main__':
    top_headlines = get_top_headlines()
    for headline in top_headlines:
        print(f'{headline["title"]}: {headline["link"]}')
