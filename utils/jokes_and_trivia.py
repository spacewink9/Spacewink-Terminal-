import requests
from bs4 import BeautifulSoup
import random

def get_joke():
    """
    Get a random joke from a website.
    """
    # Define the URL to scrape for jokes
    url = "https://www.rd.com/list/jokes-for-adults/"

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the joke cards on the page
    joke_cards = soup.find_all("div", class_="card-content")

    # Choose a random joke from the cards
    joke_card = random.choice(joke_cards)

    # Extract the setup and punchline of the joke
    setup = joke_card.find("h2").text.strip()
    punchline = joke_card.find("p").text.strip()

    # Combine the setup and punchline into a single string
    joke = setup + " " + punchline

    # Return the joke
    return joke

def get_trivia(category=None):
    """
    Get a random trivia question from a website.
    """
    # Define the URL to scrape for trivia
    url = "https://www.triviaquestionsnow.com/"

    # If a category is specified, add it to the URL
    if category:
        url += f"category-{category}-1.html"

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the trivia questions on the page
    trivia_questions = soup.find_all("div", class_="main-content-text")

    # Choose a random trivia question
    trivia_question = random.choice(trivia_questions)

    # Extract the question and answer of the trivia
    question = trivia_question.find("h4").text.strip()
    answer = trivia_question.find("p").text.strip()

    # Combine the question and answer into a single string
    trivia = question + " " + answer

    # Return the trivia
    return trivia
