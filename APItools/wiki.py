from wikipedia import wikipedia
import requests

class wikipedia_API:

    def __init__(self):
        self.sentence = 1
#todo you need to figure out how to deal with less specific search term
    #web scrapes wikidedia page for search term then get one sentence of summary
    def get_wiki_snippet(self, search_term):
        result = wikipedia.summary(search_term, sentences=self.sentence)
        return result


# re =wikipedia.page("Thanksgiving")
# rs = wikipedia.search("thanksgiving")
# th = wikipedia.summary('thanksgiving', sentences=3)
# print(th)




