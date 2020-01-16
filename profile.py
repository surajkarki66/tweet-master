from credentials.auth import Authentication
import tweepy as t


class Profile:
    def __init__(self):
        self.bot = Authentication()
        self.api = t.API(self.bot.authenticate(), wait_on_rate_limit=True, wait_on_rate_limit_notify=True)



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


    def get_messages(self):
        self.message = self.api.list_direct_messages()

        messages = [{'sender':self.api.get_user(i.message_create['sender_id']).name, 'reciever':self.api.get_user(i.message_create['target']['recipient_id']).name, 
                                    'messages':i.message_create['message_data']['text']} for i in self.message]

           
        return messages

            

 

