from credentials.auth import Authentication
import tweepy as t


class Profile:
    def __init__(self):
        self.bot = Authentication()
        self.api = t.API(self.bot.authenticate())



    def profile(self):
        self.me = self.api.me()
        name = self.me.name
        followers_count = self.me.followers_count
        following_count = self.me.friends_count
        profile = [{'name':name, 'follower_count':followers_count, 'following_count':following_count}]
        return profile


    def get_following(self):
        self.me = self.api.me()
        self.friends = self.me.friends()
        
        friends = [{'name':friend.name, 'followers_count':friend.followers_count} for friend in self.friends ]
        return friends

    
    def get_followers(self):
        self.followers = self.api.followers()
        friends = [{'name':friend.name, 'followers_count':friend.followers_count} for friend in self.followers ] 
        return friends


