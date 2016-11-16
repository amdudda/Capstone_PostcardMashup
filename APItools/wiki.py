from wikipedia import wikipedia
from contextlib import suppress
import warnings
import requests

class wikipedia_API:

    def __init__(self):
        self.sentence = 1
#todo you need to figure out how to deal with less specific search term
    #web scrapes wikidedia page for search term then get one sentence of summary
    def get_wiki_snippet(self, search_term):
        result = wikipedia.summary(search_term, sentences=self.sentence)
        return result

# debugging
if __name__ == '__main__':
    # re = wikipedia.page("Thanksgiving")
    # rs = wikipedia.search("thanksgiving")
    th = None

    # this isgnores all warnings raised - this is not without risks - see https://docs.python.org/2/library/warnings.html
    warnings.filterwarnings('ignore')
    try:
        # with suppress(UserWarning):
        th = wikipedia.summary('thing', sentences=3)
        # print(th)
    except wikipedia.DisambiguationError as de:
        th = ("A disambiguation page was reached, with the following choices:\n" + str(de.options))
    finally:
        print(th)





