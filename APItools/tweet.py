import tweepy
from APItools.APIkeys import twitter_keys
# from tweepy import OAuthHandler
# from tweepy import Stream
# from tweepy.streaming import StreamListener, json


def get_twitter(search_for="Thanksgiving"):
    auth = tweepy.OAuthHandler(twitter_keys['CONSUMER_KEY'], twitter_keys['CONSUMER_SECRET'])
    auth.set_access_token(twitter_keys['ACCESS_TOKEN'], twitter_keys['ACCESS_TOKEN_SECRET'])

    api = tweepy.API(auth)


    results = api.search(q="Thanksgiving", count=1)

    # For debugging
    # for result in results:
    #     print("\n ** Result: "+result.text)

    return results[0].text



def on_error(self, status_code):
    print('Got an error with status code: ' + str(status_code))
    return True  # To continue listening


def on_timeout(self):
    print('Timeout...')
    return True  # To continue listening



if __name__ == '__main__':
    print(get_twitter('Thanksgiving'))

# print(get_twitter())

# # Get data from twitter api
# class get_twitter(StreamListener):
#
#     def on_data(self, text):
#         print(text) # TODO error handling
#         return True
#
#     def on_error(self, status):
#         print("Could't find data. Status: "+status)
#
#
# if __name__ == '__main__':
#
#     # Handling Twitter authetification and the connection to Twitter API
#     t = get_twitter()
#     auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#     auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#     twitterstream = Stream(auth, get_twitter())
#
#     # Filtering Twitter with keyword 'Thanksgiving'
#     twitterstream.filter(track=["Thanksgiving"])
