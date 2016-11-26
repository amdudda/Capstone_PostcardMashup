from django.shortcuts import render
from . models import API_model as mod
from APItools.API_Manager import get_image, get_tweet, get_wiki_content, threaded_search


def index(request):
    # The `POST` has the data from the HTML form that was submitted.
    # ORM queries the database for all of the to-do entries.
    if request.method == 'GET':
        return render(request, 'PostcardApp/index.html')
    elif request.method == 'POST':
            search_keyword = request.POST.get('search')
            # use threading to speed up searching
            p_card_data = threaded_search(search_keyword)
            # if pixabay didn't return anything, substitute our default image instead
            # TODO create a default image
            # encoding our data as utf-8 lets us cope with non-ascii text...
            if not p_card_data['image']: p_card_data['image'] = "/images/no_results.jpg"
            Postcard_items = mod.objects.create(image=p_card_data['image'],
                                                wiki_sentence=p_card_data['wiki'].encode('utf-8'),
                                                tweet_text=p_card_data['tweet'].encode('utf-8'),
                                                search_string = search_keyword
                                                )
            # Postcard = mod.objects.all()
            # return the newly-created postcard
            return render(request, 'PostcardApp/index.html', {'Postcard': Postcard_items})

# AMD: I think my changes make this obsolete!  Now with threading!  :-D
# def result(search_keyword):
#     # DONE: take advantage of threading in API_Manager via threaded_search
#     Postcard_data = []
#     Pixabay_Image = get_image(search_keyword)
#     Wiki_snip = get_wiki_content(search_keyword)
#     tweet_txt = (get_tweet(search_keyword))
#     if Pixabay_Image:
#         Postcard_data.append(Pixabay_Image)
#     else:
#         Postcard_data.append("No image found")
#
#     if Wiki_snip:
#         Postcard_data.append(Wiki_snip)
#     else:
#         Postcard_data.append("No wiki snippet found")
#     if tweet_txt:
#         Postcard_data.append(tweet_txt) # get a tweet
#     else:
#         Postcard_data.append("No tweet found")
#
#     return Postcard_data



