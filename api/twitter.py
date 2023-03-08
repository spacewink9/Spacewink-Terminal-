import tweepy

class TwitterAPI:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        self.api = tweepy.API(auth)

    def tweet(self, message):
        try:
            self.api.update_status(status=message)
            print(f"Tweet sent: {message}")
        except tweepy.TweepError as e:
            print(f"Error sending tweet: {e}")
