import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener, json



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


results = api.search(q="Thanksgiving", count=1)


for result in results:
    print("\n ** Result: "+result.text)


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
