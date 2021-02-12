import re
import time
import json
import matplotlib.pyplot as plt

from textblob import TextBlob
from tweepy.streaming import StreamListener
from tweepy import Stream

from credentials.auth import Authentication


class StreamTweet:
    def __init__(self, username):
        self.auth = Authentication().authenticate_user()
        self.username = username

    def stream(self):
        listener = TwitterStream()
        stream = Stream(self.auth, listener)
        #stream.filter(follow=['44196397'], is_async=True)
        stream.filter(track=[self.username], is_async=True)


class TwitterStream(StreamListener):
    def __init__(self):
        super().__init__()
        plt.ion()
        self.positive = 0
        self.negative = 0
        self.compound = 0
        self.count = 0
        self.initime = time.time()

    def calctime(self, a):
        return time.time() - a

    def on_data(self, data):
        t = int(self.calctime(self.initime))
        all_data = json.loads(data)
        tweet = all_data["text"]
        # username = all_data["user"]["screen_name"]
        tweet = " ".join(re.findall("[a-zA-Z]+", tweet))

        blob = TextBlob(tweet.strip())
        self.count += 1

        sentiment = 0
        for sen in blob.sentences:
            if sen.sentiment.polarity >= 0:
                self.positive = self.positive + sen.sentiment.polarity
            else:
                self.negative = self.negative + sen.sentiment.polarity
        self.compound = self.compound + sentiment
        print(tweet.strip())
        print(sentiment)

        print(str(self.positive) + ' ' +
              str(self.negative) + ' ' + str(self.compound))
        plt.axis([0, 100, -20, 20])
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        plt.plot([t], [self.positive], 'go', [t], [
                 self.negative], 'ro', [t], [self.compound], 'bo')
        plt.show()
        plt.pause(0.0001)
        if self.count == 100:
            return False
        else:
            return True

    def on_error(self, status):
        print(status)
