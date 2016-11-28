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


def get_image(my_args):
    search = my_args[0]
    pm_data = my_args[1]
    image = get_image_url(search, pixabaykey)
    time.sleep(.5)  # pretend  do some work.
    with print_lock:
        # print("I am the pic \n", image)
        pm_data['image'] = image



def get_wiki_content(my_args):
    search = my_args[0]
    pm_data = my_args[1]
    wiki_snippet = wikiapi.get_wiki_snippet(search)
    time.sleep(.5)  # pretend  do some work.
    with print_lock:
        # print("I am the wiki snippet \n", wiki_snippet)
        pm_data['wiki'] = wiki_snippet



def get_tweet(my_args):
    search = my_args[0]
    pm_data = my_args[1]
    tweet = get_twitter(search)
    time.sleep(.5)  # pretend  do some work.
    with print_lock:
        # print("I am the tweet: \n", tweet)
        pm_data['tweet'] = tweet



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
    pm_data = {}
    # thread_params = (search,dict)
    q.put((search,pm_data))

    # wait until the thread terminates.
    q.join()

    print('Entire job took:', time.time() - start)

    return pm_data




