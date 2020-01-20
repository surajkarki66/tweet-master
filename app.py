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
            "6": self.quit

        }

    @staticmethod
    def display():
        print("""
        WELCOME TO TWITTER BOT
        1. To See Your Profile
        2. To see Your Follower
        3. To see Your Following
        4. To see Your Messages
        5. To exit
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

    def quit(self):
        sys.exit(1)


if __name__ == "__main__":
    Menu().run()
