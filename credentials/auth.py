import tweepy as t
import keys


class Authentication:
    def __init__(self):
        self.consumer_key = keys.consumer_key
        self.consumer_secret = keys.consumer_secret
        self.access_token = keys.access_token
        self.access_token_secret =keys.access_token_secret

    def authenticate(self):
        auth = t.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return auth
