import requests
from typing import List
from datetime import datetime

class NewsAPI:
    """
    A class to interact with the news API and retrieve news articles.
    """

    def __init__(self, api_key: str):
        """
        Initializes the NewsAPI class.

        :param api_key: A string with the API key.
        """
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/"

    def search(self, query: str, sources: List[str] = None, language: str = "en", from_date: datetime = None,
               to_date: datetime = None, sort_by: str = "publishedAt", page: int = 1) -> List[dict]:
        """
        Search for news articles that match the given query.

        :param query: A string with the search query.
        :param sources: A list of strings with the news sources to search from. Default is None (all sources).
        :param language: A string with the language of the news articles. Default is "en" (English).
        :param from_date: A datetime object with the start date of the search range. Default is None (no start date).
        :param to_date: A datetime object with the end date of the search range. Default is None (no end date).
        :param sort_by: A string with the sorting method for the results. Default is "publishedAt".
        :param page: An integer with the page number of the results. Default is 1.
        :return: A list of dictionaries with the news articles.
        """
        params = {
            "apiKey": self.api_key,
            "q": query,
            "language": language,
            "sortBy": sort_by,
            "page": page
        }
        if sources is not None:
            sources_str = ",".join(sources)
            params["sources"] = sources_str
        if from_date is not None:
            params["from"] = from_date.strftime("%Y-%m-%d")
        if to_date is not None:
            params["to"] = to_date.strftime("%Y-%m-%d")

        response = requests.get(f"{self.base_url}everything", params=params)
        if response.status_code == 200:
            data = response.json()
            return data["articles"]
        else:
            raise ValueError(f"Failed to retrieve news articles. Error code: {response.status_code}")

