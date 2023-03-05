import tweepy
from textblob import TextBlob

CONSUMER_KEY = 'your_consumer_key_here'
CONSUMER_SECRET = 'your_consumer_secret_here'
ACCESS_TOKEN = 'your_access_token_here'
ACCESS_TOKEN_SECRET = 'your_access_token_secret_here'
COMPANY_NAME = 'Apple'  # Replace with the name of the company you want to search for

def authenticate_twitter_api():
    """
    Authenticates the Tweepy library with Twitter API using API keys.
    
    Returns:
    A tweepy.API object representing the authenticated Twitter API.
    """
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

def get_company_tweets(api):
    """
    Fetches recent tweets about a specific company from Twitter API.
    
    Args:
    api: A tweepy.API object representing the authenticated Twitter API.
    
    Returns:
    A list of strings, where each string represents the text content of a tweet.
    """
    company_tweets = []
    for tweet in tweepy.Cursor(api.search, q=COMPANY_NAME, lang='en', tweet_mode='extended').items(100):
        if 'retweeted_status' in tweet._json:
            tweet_text = tweet._json['retweeted_status']['full_text']
        else:
            tweet_text = tweet.full_text
        company_tweets.append(tweet_text)
    return company_tweets

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
    api = authenticate_twitter_api()
    company_tweets = get_company_tweets(api)
    for tweet in company_tweets:
        sentiment = perform_sentiment_analysis(tweet)
        print(f'{sentiment}: {tweet}')
