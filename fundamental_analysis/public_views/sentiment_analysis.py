import requests
from textblob import TextBlob

API_KEY = 'your_api_key_here'
COMPANY_NAME = 'Apple'  # Replace with the name of the company you want to search for
API_URL = f'https://api.news.com/company-news?q={COMPANY_NAME}&apiKey={API_KEY}'

def get_company_news():
    """
    Fetches recent news articles about a specific company from a news API.
    
    Returns:
    A list of strings, where each string represents the text content of a news article.
    """
    response = requests.get(API_URL)
    if response.ok:
        data = response.json()
        articles = data['articles']
        company_news = []
        for article in articles:
            company_news.append(article['content'])
        return company_news
    else:
        raise ValueError(f'Error fetching company news: {response.text}')

def perform_sentiment_analysis(text):
    """
    Performs sentiment analysis on a given text using TextBlob library.
    
    Args:
    text: A string representing the text to be analyzed.
    
    Returns:
    A string representing the sentiment of the text, which can be either 'positive', 'neutral', or 'negative'.
    """
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return 'positive'
    elif sentiment_score < 0:
        return 'negative'
    else:
        return 'neutral'

if __name__ == '__main__':
    company_news = get_company_news()
    for article in company_news:
        sentiment = perform_sentiment_analysis(article)
        print(f'{sentiment}: {article}')
