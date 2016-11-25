from APItools.Pixabay import *
from APItools.tweet import *
from APItools.wiki import wikipedia_API as wikiapi
import threading
from queue import Queue
import time

"""This is taken from: - https://pythonprogramming.net/threading-tutorial-python/"""
""" This class does the book-search on the basis of four different keywords given using multi-threading"""

# putting a lock so that no other funtion can call it when other is using
print_lock = threading.Lock()
pixabaykey=''


def get_image(search):
    image = get_image_url(search, pixabaykey)
    time.sleep(.5)  # pretend  do some work.
    with print_lock:
        print("I am the pic \n", image)
        return image



def get_wiki_content(search):
    wiki_snippet = wikiapi.get_wiki_snippet(search)
    time.sleep(.5)  # pretend  do some work.
    with print_lock:
        print("I am the wiki snippet \n", wiki_snippet)
        return wiki_snippet



def get_tweet(search):
    tweet = get_twitter(search)
    time.sleep(.5)  # pretend  do some work.
    with print_lock:
        print("I am the tweet: \n", tweet)
        return tweet



def threader():
    while True:
        # gets an worker from the queue
        searcher = q.get()
        # Run the example job with the avail worker in queue (thread)
        get_image(searcher)
        get_wiki_content(searcher)
        get_tweet(searcher)
        # completed with the job
        q.task_done()

q = Queue()

def threaded_search(search_for="Thanksgiving"):
    # how many threads are we going to allow for
    for x in range(5):
        image = threading.Thread(name='image-search', target=threader)
        wiki = threading.Thread(name='wiki-snippet', target=threader)
        tweet= threading.Thread(name='tweet-snippet', target=threader)
        # classifying as a daemon, so they will die when the main dies
        image.daemon = True
        wiki.daemon = True
        tweet.daemon = True
        # begins, must come after daemon definition
        image.start()
        wiki.start()
        tweet.start()

    start = time.time()
    # list of random search string- can change it as per your choice
    search = [search_for]
    q.put(search)

    # wait until the thread terminates.
    q.join()

    print('Entire job took:', time.time() - start)




