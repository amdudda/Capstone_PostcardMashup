from wikipedia import wikipedia
from contextlib import suppress
import warnings
import random
import requests


# class created by Marian
class wikipedia_API:
    def __init__(self):
        self.sentence = 1
        self.recursion_count = 0
        self.snippet = ""
    # todo you need to figure out how to deal with less specific search term
    # web scrapes wikipedia page for search term then get one sentence of summary

    def get_wiki_snippet(self, search_term):

        # https://docs.python.org/3/library/warnings.html#temporarily-suppressing-warnings the link to chatch warning
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            while True:
                try:
                    result = wikipedia.summary(search_term)
                    print(result)
                    return
                except wikipedia.DisambiguationError as e:
                    print(e.options)
                except wikipedia.PageError as err:
                    result = "No matches found for " + str(search_term)
                    print(result)
                    print("Here is the error", err)
                    break
                finally:
                    break


# debugging
if __name__ == '__main__':
    search_term = "summer"
    disambiguation_error_search = "thing"
    page_error_search = "qroiew af 8phqifnea f "
    terms = [search_term, disambiguation_error_search,page_error_search]
    for srch in terms:
        print("searching for '" + srch + "'...")
        w = wikipedia_API()
        w.get_wiki_snippet(srch)
        print(w.snippet)



