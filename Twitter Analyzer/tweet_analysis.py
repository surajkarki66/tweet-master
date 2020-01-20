import time
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import re
from tweepy.streaming import StreamListener
from tweepy import Stream

from credentials.auth import Authentication


class StreamTweet:
    def __init__(self):
        self.auth = Authentication().authenticate_user()

    def stream(self):
        listener = TwitterStream()
        stream = Stream(self.auth, listener)
        #stream.filter(follow=['44196397'], is_async=True)
        stream.filter(track=['Donald Trump'], is_async=True)


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
            senti = sentiment + sen.sentiment.polarity
            if sen.sentiment.polarity >= 0:
                self.positive = self.positive + sen.sentiment.polarity
            else:
                self.negative = self.negative + sen.sentiment.polarity
        self.compound = self.compound + sentiment
        print(self.count)
        print(tweet.strip())
        print(sentiment)
        print(t)

        print(str(self.positive) + ' ' + str(self.negative) + ' ' + str(self.compound))
        plt.axis([0, 100, -20, 20])
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        plt.plot([t], [self.positive], 'go', [t], [self.negative], 'ro', [t], [self.compound], 'bo')
        plt.show()
        plt.pause(0.0001)
        if self.count == 200:
            return False
        else:
            return True

    def on_error(self, status):
        print(status)


a = StreamTweet()
a.stream()
