import requests
from bs4 import BeautifulSoup

def search_recipe(query):
    # Use a search engine to fetch recipe data
    search_url = f'https://www.google.com/search?q={query} recipe'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract recipe data from search results
    recipe_card = soup.find('div', class_='ZINbbc xpd O9g5cc uUPGi')
    recipe_title = recipe_card.find('div', class_='BNeawe s3v9rd AP7Wnd').text
    recipe_description = recipe_card.find('div', class_='BNeawe s3v9rd XbiCqe').text
    recipe_url = recipe_card.find('a')['href']

    # Print the recipe details
    print(f"Title: {recipe_title}")
    print(f"Description: {recipe_description}")
    print(f"URL: {recipe_url}")
