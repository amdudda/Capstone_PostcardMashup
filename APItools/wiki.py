from wikipedia import wikipedia
from contextlib import suppress
import warnings
import random
import requests

class wikipedia_API:
# class created by Marian

    def __init__(self):
        self.sentence = 1
        self.recursion_count=0
        self.snippet=""
#todo you need to figure out how to deal with less specific search term
    #web scrapes wikidedia page for search term then get one sentence of summary
    def get_wiki_snippet(self, search_term):

        #https://docs.python.org/3/library/warnings.html#temporarily-suppressing-warnings the link to chatch warning
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            while True:
                try:
                    result = wikipedia.summary(search_term, sentences=self.sentence)
                    # self.snippet = result
                    break
                except wikipedia.DisambiguationError as e:
                    # AMD: grab a random article from the disambiguation options (we KNOW it's valid) and return that.
                    the = random.choice(e.options)
                    result = wikipedia.summary(the,sentences=self.sentence)
                    # self.snippet = result
                    break
                except wikipedia.PageError as err:
                    # AMD: tell the user we found no results - that's what PageError means
                    # result = self.recusive_error(search_term)
                    result = "No matches found for " + str(search_term)
                    break
                finally:
                    self.snippet = result
        #self.recursion_count=0
        # return result
    def recusive_error(self, search_term):
        self.recursion_count+=1
        print('recursion #'+ str(self.recursion_count))
        try:
            result = wikipedia.summary(search_term, sentences=self.sentence)

        except wikipedia.DisambiguationError as e:
            print(search_term)
            the = random.choice(e.options)
            result = self.recusive_error(the)
        except wikipedia.PageError as err:
            result = self.recusive_error(search_term)

        return result

# debugging
if __name__ == '__main__':
#     # re = wikipedia.page("Thanksgiving")
#     # rs = wikipedia.search("thanksgiving")
#     th = None
#
#     # this isgnores all warnings raised - this is not without risks - see https://docs.python.org/2/library/warnings.html
#     warnings.filterwarnings('ignore')
#     try:
#         # with suppress(UserWarning):
#         th = wikipedia.summary('thing', sentences=3)
#         # print(th)
#     except wikipedia.DisambiguationError as de:
#         th = ("A disambiguation page was reached, with the following choices:\n" + str(de.options))
#     finally:
#         print(th)
    search_term = "Thanksgiving"
    disambiguation_error_search = "thing"
    page_error_search = "qroiew af 8phqifnea f "
    terms = [search_term,disambiguation_error_search,page_error_search]
    for srch in terms:
        print("searching for '" + srch + "'...")
        w = wikipedia_API()
        w.get_wiki_snippet(srch)
        print(w.snippet)



