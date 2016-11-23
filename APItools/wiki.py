from wikipedia import wikipedia
from contextlib import suppress
import warnings
import random
import requests


# class created by Marian

class wikipedia_API():
    def __init__(self):
        self.sentence = 1
        self.recursion_count = 0
        self.snippet = ""
    # todo you need to figure out how to deal with less specific search term
    # web scrapes wikipedia page for search term then get one sentence of summary
    @staticmethod
    def get_wiki_snippet(search_term):
        result=""
        # https://docs.python.org/3/library/warnings.html#temporarily-suppressing-warnings the link to chatch warning
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            while True:
                try:
                    result = wikipedia.summary(search_term)
                    break
                except wikipedia.DisambiguationError as e:
                    new_article = random.choice(e.options)
                    result = wikipedia.summary(new_article)
                    break
                except wikipedia.PageError as err:
                    result = "No matches found for " + str(search_term)
                    break

        return result

# debugging
if __name__ == '__main__':
    search_term = "Thanksgiving"
    disambiguation_error_search = "thing"
    page_error_search = "qroiew af 8phqifnea f "
    terms = [search_term, disambiguation_error_search, page_error_search]
    for srch in terms:
        print("searching for '" + srch + "'...")
        w = wikipedia_API()
        snip = w.get_wiki_snippet(srch)
        print(snip)



