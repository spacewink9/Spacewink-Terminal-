import requests
from bs4 import BeautifulSoup

def get_movie_recommendation(query):
    """
    Get a movie recommendation based on user input using a search engine.
    """
    url = f"https://www.google.com/search?q={query}+movie"
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    result = soup.find(class_='BNeawe iBp4i AP7Wnd').get_text()
    return result

def get_tv_show_recommendation(query):
    """
    Get a TV show recommendation based on user input using a search engine.
    """
    url = f"https://www.google.com/search?q={query}+tv+show"
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    result = soup.find(class_='BNeawe iBp4i AP7Wnd').get_text()
    return result
