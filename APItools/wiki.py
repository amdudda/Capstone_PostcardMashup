from wikipedia import wikipedia
from contextlib import suppress
import warnings
import random
import requests

class wikipedia_API:

    def __init__(self):
        self.sentence = 1
        self.recursion_count=0
#todo you need to figure out how to deal with less specific search term
    #web scrapes wikidedia page for search term then get one sentence of summary
    def get_wiki_snippet(self, search_term):

        #https://docs.python.org/3/library/warnings.html#temporarily-suppressing-warnings the link to chatch warning
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            while True:
                try:
                    result = wikipedia.summary(search_term, sentences=self.sentence)
                    break
                except wikipedia.DisambiguationError as e:

                    the = random.choice(e.options)
                    result = self.recusive_error(the)
                except wikipedia.PageError as err:
                    result = self.recusive_error(search_term)
        #self.recursion_count=0
        return result
    def recusive_error(self, search_term):
        self.recursion_count+=1
        print('recursion #'+ str(self.recursion_count))
        try:
            result = wikipedia.summary(search_term, sentences=self.sentence)

        except wikipedia.DisambiguationError as e:

            the = random.choice(e.options)
            result = self.recusive_error(search_term)
        except wikipedia.PageError as err:
            result = self.recusive_error(search_term)

        return result

# debugging
# if __name__ == '__main__':
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





