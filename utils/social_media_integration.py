import requests

class SocialMediaAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.socialmedia.com/v1/"

    def get_user_info(self, username):
        """Get user information"""
        endpoint = f"{self.base_url}/user"
        params = {
            "api_key": self.api_key,
            "username": username
        }
        response = requests.get(endpoint, params=params)

        if response.status_code == 200:
            user_data = response.json()
            return user_data
        else:
            return None

    def post_tweet(self, message):
        """Post a tweet"""
        endpoint = f"{self.base_url}/tweet"
        params = {
            "api_key": self.api_key
        }
        data = {
            "message": message
        }
        response = requests.post(endpoint, params=params, json=data)

        if response.status_code == 200:
            tweet_data = response.json()
            return tweet_data
        else:
            return None

# Demo usage
if __name__ == '__main__':
    api_key = "demo_api_key"
    sm_api = SocialMediaAPI(api_key)

    # Get user information
    user_info = sm_api.get_user_info("john_doe")
    print(user_info)

    # Post a tweet
    tweet_data = sm_api.post_tweet("Hello, world!")
    print(tweet_data)
