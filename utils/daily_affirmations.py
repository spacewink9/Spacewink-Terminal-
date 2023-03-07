import requests
from bs4 import BeautifulSoup
import random

def get_affirmation():
    """
    Returns a random daily affirmation from the internet using web scraping.
    """
    # Make a search query on the internet for daily affirmations
    query = "daily affirmations"
    url = f"https://www.google.com/search?q={query}&rlz=1C1GCEU_enUS832US832&oq={query}&aqs=chrome.0.35i39l2j0i131i433l2j0j69i60.2204j1j4&sourceid=chrome&ie=UTF-8"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    # Parse the HTML response
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("div", class_="BNeawe iBp4i AP7Wnd")

    # Filter out any unwanted text
    affirmations = [result.get_text() for result in results if "affirmation" in result.get_text().lower()]

    # Select a random affirmation from the list
    affirmation = random.choice(affirmations)

    # Return the affirmation
    return affirmation
