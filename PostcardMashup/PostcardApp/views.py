from django.shortcuts import render
from .models import API_model as mod
from APItools.API_Manager import threaded_search


def index(request):
    # The `POST` has the data from the HTML form that was submitted.
    # ORM queries the database for all of the to-do entries.
    unique_keywords = mod.objects.values('search_string').distinct()[:25]
    if request.method == 'GET':
        five_newest = mod.objects.order_by("-Saved_n")[:5]
        # print(five_newest)
        context = {'Postcards':five_newest,'keywords':unique_keywords}
        return render(request, 'PostcardApp/index.html', context)
    elif request.method == 'POST':
            search_keyword = request.POST.get('search')
            # use threading to speed up searching
            p_card_data = threaded_search(search_keyword)
            # if pixabay didn't return anything, substitute our default image instead
            # TODO create a default image
            # encoding our data as utf-8 lets us cope with non-ascii text...
            if not p_card_data['image']: p_card_data['image'] = "/static/no_results.jpg"
            if not p_card_data['tweet']: p_card_data['tweet'] = "No tweet found for '%s'."% search_keyword
            Postcard_items = mod.objects.create(image=p_card_data['image'],
                                                wiki_sentence=p_card_data['wiki'].encode('utf-8'),
                                                tweet_text=p_card_data['tweet'].encode('utf-8'),
                                                search_string = search_keyword
                                                )
            # font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 25)
            # return the newly-created postcard
            context = {'Postcards': [Postcard_items,], 'keywords': unique_keywords}
            return render(request, 'PostcardApp/index.html', context)

def keyword(request,sk):
    # get all postcards that match the search term
    print("sk is: " + sk)
    Postcard_items = mod.objects.filter(search_string=sk)

    unique_keywords = mod.objects.values('search_string').distinct()[:25]
    context = {'Postcards': Postcard_items, 'keywords':unique_keywords}

    # then pass them to index to render them
    return render(request,'PostcardApp/index.html', context)


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



