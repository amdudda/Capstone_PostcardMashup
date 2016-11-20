from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

# ***  You will need api key to be able to run it.
# TODO apikye

# Get data from twitter api
class get_twitter(StreamListener):

    def on_data(self, text):
        print(text) # TODO error handling
        return True

    def on_error(self, status):
        print("Could't find data. Status: "+status)


if __name__ == '__main__':

    # Handling Twitter authetification and the connection to Twitter API
    t = get_twitter()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    twitterstream = Stream(auth, get_twitter())

    # Filtering Twitter with keyword 'Thanksgiving'
    twitterstream.filter(track=["Thanksgiving"])