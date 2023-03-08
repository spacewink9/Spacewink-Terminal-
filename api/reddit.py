import praw
from typing import List

class RedditAPI:
    """
    A class for interacting with the Reddit API.
    """

    def __init__(self, client_id: str, client_secret: str, user_agent: str):
        """
        Initialize the Reddit API client.

        :param client_id: The client ID provided by Reddit.
        :param client_secret: The client secret provided by Reddit.
        :param user_agent: A unique identifier for the application.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

    def get_hot_posts(self, subreddit: str, limit: int = 10) -> List[dict]:
        """
        Get the hot posts in a subreddit.

        :param subreddit: The subreddit to retrieve posts from.
        :param limit: The maximum number of posts to retrieve.
        :return: A list of dictionaries representing the hot posts in the subreddit.
        """
        subreddit = self.reddit.subreddit(subreddit)
        hot_posts = subreddit.hot(limit=limit)
        post_list = []
        for post in hot_posts:
            post_dict = {
                "title": post.title,
                "author": post.author.name,
                "score": post.score,
                "created_utc": post.created_utc,
                "url": post.url,
                "num_comments": post.num_comments
            }
            post_list.append(post_dict)
        return post_list

    def get_trending_subreddits(self, limit: int = 10) -> List[str]:
        """
        Get the currently trending subreddits.

        :param limit: The maximum number of subreddits to retrieve.
        :return: A list of the top trending subreddits.
        """
        trends = self.reddit.subreddit("trendingsubreddits").hot(limit=limit)
        subreddit_list = []
        for trend in trends:
            subreddit_list.append(trend.title)
        return subreddit_list

    def search_subreddits(self, query: str, limit: int = 10) -> List[str]:
        """
        Search for subreddits based on a query.

        :param query: The search query.
        :param limit: The maximum number of subreddits to retrieve.
        :return: A list of subreddits matching the query.
        """
        subreddits = self.reddit.subreddits.search(query, limit=limit)
        subreddit_list = []
        for subreddit in subreddits:
            subreddit_list.append(subreddit.display_name)
        return subreddit_list

    def get_subreddit_info(self, subreddit: str) -> dict:
        """
        Get information about a subreddit.

        :param subreddit: The name of the subreddit.
        :return: A dictionary containing information about the subreddit.
        """
        subreddit = self.reddit.subreddit(subreddit)
        info_dict = {
            "name": subreddit.display_name,
            "title": subreddit.title,
            "description": subreddit.public_description,
            "subscribers": subreddit.subscribers,
            "created_utc": subreddit.created_utc,
            "url": subreddit.url,
            "over18": subreddit.over18
        }
        return info_dict
