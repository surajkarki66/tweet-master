import tweepy as t


consumer_key = 'cybcnsHSMiyi0aAmLkb2I17jd'
consumer_secret = 'mW7ormNjJuhv051bh9giGTmKv6RecsEJhjorZv2tGY1CFLjmZa'
access_token = '2896323368-zobzdN9hqpSdepwKVN1XpMuoOM0drCTKUbTLkch'
access_token_secret = 'd9qwRG1Qc6xgg2GRUQZ7FMs9PGMEAZlr3Mm48Sxo8Ac1e'




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
