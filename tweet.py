from credentials.auth import Authentication
import tweepy as t


class Tweet:
    def __init__(self):
        self.bot = Authentication()
        self.api = t.API(self.bot.authenticate(), wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # GET Requests

    def user_tweets(self):
        username = 'Surazz karkey'
        self.user_stat = self.api.user_timeline(username)
        

        user_tweet = [{'text': i.text, 'likes': i.favorite_count, 'retweet': i.retweet_count,
                        'isRetweeted': i.retweeted, 'reply_to': i.in_reply_to_screen_name,
                        'created_at': i.created_at} for i in self.user_stat]

        return user_tweet


    def followers_tweet(self):
        self.tweets = self.api.home_timeline()

        tweets = [{'text':i.text, 'author':i.user.name,
                    'likes':i.favorite_count, 'created_at': i.created_at} for i in self.tweets]
        return tweets
      

