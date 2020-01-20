import sys

from main.profile import Profile
from main.tweet import Tweet


class Menu:
    def __init__(self):
        self.profile = Profile()
        self.tweet = Tweet()
        self.choices = {
            "1": self.show_profile,
            "2": self.show_followers,
            "3": self.show_following,
            "4": self.show_messages,
            "5": self.send_message_all,
            "6": self.send_individual,
            "7": self.user_tweets,
            "8": self.followers_tweets,
            "9": self.user_retweets,
            "10": self.specified_user_tweets,
            "11": self.like_all,
            "12": self.like_specified,
            "13": self.retweet_all,
            "14": self.retweet_specified,
            "15": self.reply_all,
            "16": self.reply_specific,
            "17": self.quit

        }

    @staticmethod
    def display():
        print("""
        WELCOME TO TWITTER BOT
        1. To See Your Profile
        2. To see Your Follower
        3. To see Your Following
        4. To see Your Messages
        5. To send message to all
        6. To send message individually
        7. To see user tweets
        8. To see friends tweets
        9. To see retweets of me
        10. To see specified user tweets
        11. To like all tweets
        12. To like specified user status
        13. To retweet all home status
        14. To retweet specified user
        15. To reply all post
        16. To reply specific post
        17. To quit
        """)

    def run(self):
        while True:
            self.display()
            choice = input("Enter your choice:")
            print("\n")
            action = self.choices.get(choice)

            if action:
                action()

            else:
                print("Not a valid input")

    def show_profile(self):
        profile = self.profile.profile()
        for p in profile:
            print(f'Username:', p['name'])
            print(f'Followers:', p['follower_count'])
            print(f'Following:', p['following_count'])
            print('')

    def show_followers(self):
        followers = self.profile.get_followers()
        for f in followers:
            print('Name:', f['name'])
            print('Followers_Count:', f['followers_count'])
            print('Following', f['friends_count'])
            print('')

    def show_following(self):
        followings = self.profile.get_following()
        for f in followings:
            print('Name:', f['name'])
            print('Followers_Count:', f['followers_count'])
            print('Following', f['friends_count'])
            print('Is Verified', f['isVerified'])
            print('Profile Image:', f['profile_image'])
            print('')

    def show_messages(self):
        messages = self.profile.get_messages()
        for m in messages:
            print('Recipient_ID:', m['recipient_id'])
            print('Receiver:', m['receivers'])
            print('Messages:', m['messages'])
            print('')

    def send_message_all(self):
        text = str(input("Enter the message:"))
        self.profile.post_messages(text)
        print('Message successfully sent.')

    def send_individual(self):
        text = str(input("Enter the message:"))
        r_id = str(input("Enter the recipient id:"))
        self.profile.send_individual(text, r_id)
        print('Message successfully sent.')

    def user_tweets(self):
        print("Your tweets are:")
        tweet = self.tweet.user_tweets()
        for t in tweet:
            print('Text:', t['text'])
            print('Likes:', t['likes'])
            print('Retweet_Count:', t['retweet'])
            print('Is Retweeted:', t['isRetweeted'])
            print('Reply To:', t['reply_to'])
            print('Created At:', t['created_at'])
            print('')

    def followers_tweets(self):
        print("Your friends tweets are")
        tweet = self.tweet.followers_tweet()
        for t in tweet:
            print('Text:', t['text'])
            print('Likes:', t['likes'])
            print('Author:', t['author'])
            print('Created At:', t['created_at'])
            print('')

    def user_retweets(self):
        print("Your Retweets are:")
        retweets = self.tweet.retweets_of_me()
        for t in retweets:
            print('Text:', t['text'])
            print('Likes:', t['likes'])
            print('Author:', t['author'])
            print('Created At:', t['created_at'])
            print('')

    def specified_user_tweets(self):
        name = str(input("Enter the username:"))
        print(f'Tweets of {name} are:')
        tweets = self.tweet.get_specified_user_status(name)
        for t in tweets:
            print('Text:', t['text'])
            print('Likes:', t['likes'])
            print('Author:', t['author'])
            print('Created At:', t['created_at'])
            print('')

    def like_all(self):
        like = self.tweet.like_tweet()
        print("Liked")

    def like_specified(self):
        name = str(input("Enter the name:"))
        self.tweet.like_specified_user_status(name)
        print(f'Liked {name} status ')

    def retweet_all(self):
        self.tweet.retweet()

    def retweet_specified(self):
        name = str(input("Enter the name:"))
        self.tweet.retweet_specified_user_status(name)
        print(f'Retweeted to {name} post')

    def reply_all(self):
        message = input("Enter the message:")
        self.tweet.reply_to_tweet(message)
        print('Replied all')

    def reply_specific(self):
        name = input("Enter the name:")
        message = input("Enter the message:")
        self.tweet.reply_to_specified_user_tweet(message, name)





    def quit(self):
        sys.exit(1)


if __name__ == "__main__":
    Menu().run()
