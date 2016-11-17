from wikipedia import wikipedia
from contextlib import suppress
import warnings
import random
import requests

class wikipedia_API:

    def __init__(self):
        self.sentence = 1
#todo you need to figure out how to deal with less specific search term
    #web scrapes wikidedia page for search term then get one sentence of summary
    def get_wiki_snippet(self, search_term):
        #https://docs.python.org/3/library/warnings.html#temporarily-suppressing-warnings the link to chatch warning
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            try:
                result = wikipedia.summary(search_term, sentences=self.sentence)
            except wikipedia.DisambiguationError as e:

                the = random.choice(e.options)
                result = wikipedia.summary(the, sentences=self.sentence)


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





