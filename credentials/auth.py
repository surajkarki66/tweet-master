import tweepy as t


consumer_key = '6V9cUc5RtzqePAs4VIQtOHn1f'
consumer_secret = 'p4aL79b0KFdNLscOBnttJhhXxD3PjrAT2oiijp7Mh6htpd2xix'
access_token = '2896323368-Uk0ofBKyBKfiITbpD9D7wgl522lrbL1g3w2GVFp'
access_token_secret = 'FHwk3CvgsuawjVmmDpLCrW97jryU9aUlh2G0J9t8PTMOu'




class Authentication:
    def __init__(self):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def authenticate(self):
        auth = t.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return auth
