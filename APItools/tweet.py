import tweepy
from APItools.APIkeys import twitter_keys


def get_twitter(search):
    auth = tweepy.OAuthHandler(twitter_keys['CONSUMER_KEY'], twitter_keys['CONSUMER_SECRET'])
    auth.set_access_token(twitter_keys['ACCESS_TOKEN'], twitter_keys['ACCESS_TOKEN_SECRET'])

    api = tweepy.API(auth)
    results = api.search(q=search, count=1)
    return results[0].text

