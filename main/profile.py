from credentials import auth
import tweepy as t


class Profile:
    def __init__(self):
        self.bot = auth.Authentication()
        self.api = t.API(self.bot.authenticate_user(), wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # GET Requests

    def profile(self):
        me = self.api.me()
        name = me.name
        followers_count = me.followers_count
        following_count = me.friends_count
        profile = [{'name': name, 'follower_count': followers_count, 'following_count': following_count}]
        return profile

    def get_following(self):
        me = self.api.me()
        friends = me.friends()
        friends = [
            {'name': friend.name, 'followers_count': friend.followers_count, 'friends_count': friend.friends_count,
             'isVerified': friend.verified,
             'profile_image': friend.profile_image_url_https} for friend in friends]
        return friends

    def get_followers(self):
        followers = self.api.followers()
        friends = [{'name': friend.name, 'followers_count': friend.followers_count,
                    'friends_count': friend.friends_count,
                    'isVerified': friend.verified,
                    'profile_image': friend.profile_image_url_https} for friend in followers]
        return friends

    def get_messages(self):
        message = self.api.list_direct_messages()
        messages = [{'senders': self.api.get_user(i.message_create['sender_id']).name,
                     'receivers': self.api.get_user(i.message_create['target']['recipient_id']).name,
                     'messages': i.message_create['message_data']['text']} for i in message]

        return messages

    @staticmethod
    def remove_duplicates(self, list_of_id):
        unique_list = []

        for e in list_of_id:
            if e not in unique_list:
                unique_list.append(e)

        return unique_list

    # POST request
    def post_messages(self, text):
        recipient_id_text = open('../recipient_id.txt', "w")
        message = self.api.list_direct_messages()
        for i in message:
            recipient_id = i.message_create['target']['recipient_id']
            recipient_id_text.writelines(str(recipient_id) + '\n')

        recipient_id_text.close()

        f_read = open('../recipient_id.txt', 'r')
        r_Id = f_read.readlines()
        r_Id = [line.strip() for line in r_Id]
        r_id = self.remove_duplicates(self, r_Id)
        f_read.close()
        for i in r_id:
            if i == "2896323368":
                pass
            else:
                message = self.api.send_direct_message(i, text=text)

        return message
