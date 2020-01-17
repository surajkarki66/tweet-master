from credentials.auth import Authentication
import tweepy as t


class Tweet:
    def __init__(self):
        self.bot = Authentication()
        self.api = t.API(self.bot.authenticate(), wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # GET Requests

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

    def like_tweet(self):
        tweets = self.api.home_timeline()
        try:
            for i in tweets:
                status_id = i.id
                self.api.create_favorite(status_id)
                print("Liked->", i.text, "By ", i.user.name)

        except t.TweepError as e:
            print(e.reason)

        finally:
            for i in tweets:
                print("Text", i.text, "BY->", i.user.name)
                cmd = input("Press d to dislike individual tweets\nPress s to dislike all tweets")
                if cmd == "d":
                    status_id = i.id
                    self.api.destroy_favorite(status_id)

                elif cmd == "s":
                    self.api.destroy_favorite(status_id)

                else:
                    return
