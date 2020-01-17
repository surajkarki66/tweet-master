from credentials.auth import Authentication
import tweepy as t


class Tweet:
    def __init__(self):
        self.bot = Authentication()
        self.api = t.API(self.bot.authenticate(), wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # GET

    def user_tweets(self):
        username = 'Surazz karkey'
        user_stat = self.api.user_timeline(username)
        for i in user_stat:
            status_id = i.id
            self.api.create_favorite(status_id)
            print("Liked")

        user_tweet = [{'text': i.text, 'likes': i.favorite_count, 'retweet': i.retweet_count,
                       'isRetweeted': i.retweeted, 'reply_to': i.in_reply_to_screen_name,
                       'created_at': i.created_at} for i in user_stat]

        return user_tweet

    def followers_tweet(self):
        tweets = self.api.home_timeline()
        tweets = [{'text': i.text, 'author': i.user.name,
                   'likes': i.favorite_count, 'created_at': i.created_at} for i in tweets]
        return tweets

    def retweets_of_me(self):
        retweets = self.api.retweets_of_me()
        retweet = [{'text': i.text, 'user': i.user.name,
                    'likes': i.favorite_count, 'created_at': i.created_at} for i in retweets]

        return retweet

    def get_specified_user_status(self, screenname):
        tweets = self.api.user_timeline(screenname)
        tweets = [{'status_id': i.id, 'text': i.text, 'author': i.user.name,
                   'likes': i.favorite_count, 'created_at': i.created_at} for i in tweets]
        return tweets

    # POST
    def like_tweet(self):
        tweets = self.api.home_timeline()
        for i in tweets:
            try:
                status_id = i.id
                self.api.create_favorite(status_id)
                print("Liked->", i.text, "By ", i.user.name)

            except t.TweepError as e:
                pass

    def retweet(self):
        tweets = self.api.home_timeline()
        for i in tweets:
            try:
                status_id = i.id
                self.api.retweet(status_id)
                print("retweeted on", i.text)

            except t.TweepError as e:
                print(e.reason)
                pass

    def unretweeted(self):
        tweets = self.api.home_timeline()
        for i in tweets:
            try:
                status_id = i.id
                self.api.unretweet(status_id)
                print('Unretweeted on', i.text)

            except t.TweepError as e:
                print(e.reason)
                pass

    def reply_to_tweet(self, reply_message):
        tweets = self.api.home_timeline()
        for i in tweets:
            try:
                status_id = i.id
                self.api.update_status(reply_message, status_id, auto_populate_reply_metadata=True)

            except t.TweepError as e:
                print(e.reason)
                pass

    def like_specified_user_status(self, screenname):
        tweets = self.api.user_timeline(screenname)
        for i in tweets:
            try:
                status_id = i.id
                self.api.create_favorite(status_id)
                print("Liked->", i.text, "By ", i.user.name)

            except t.TweepError as e:
                pass

    def retweet_specified_user_status(self, screenname):
        tweets = self.api.user_timeline(screenname)
        for i in tweets:
            try:
                status_id = i.id
                self.api.retweet(status_id)
                print("retweeted")

            except t.TweepError as e:
                pass

    def reply_to_specified_user_tweet(self, reply_message, screenname):
        tweets = self.api.user_timeline(screenname)
        for i in tweets:
            try:
                status_id = i.id
                self.api.update_status(reply_message, status_id, auto_populate_reply_metadata=True)

            except t.TweepError as e:
                print(e.reason)
                pass

