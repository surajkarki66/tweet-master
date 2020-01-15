from credentials.auth import Authentication
import tweepy as t


class Bot:

    def __init__(self):
        self.bot = Authentication()
        self.api = t.API(self.bot.authenticate())

    

   


