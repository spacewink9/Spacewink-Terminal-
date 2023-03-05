from screens.base_screen import BaseScreen
from utils.api import get_news_sentiment

class SentimentAnalysisScreen(BaseScreen):
    def __init__(self, terminal):
        super().__init__(terminal)

    def display(self):
        self.clear_screen()
        print("=== Sentiment Analysis Screen ===")
        keyword = self.get_user_input("Enter keyword to analyze: ")

        # Get sentiment for keyword
        sentiment = get_news_sentiment(keyword)

        # Display results
        print(f"\nSentiment for '{keyword}': {sentiment}")
