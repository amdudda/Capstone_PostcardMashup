from django.shortcuts import render
from . models import API_model as mod
from APItools.API_Manager import get_image, get_tweet, get_wiki_content


def index(request):
    # The `POST` has the data from the HTML form that was submitted.
    # ORM queries the database for all of the to-do entries.
    if request.method == 'GET':
        return render(request, 'PostcardApp/index.html')
    elif request.method == 'POST':
            search_keyword = request.POST.get('search')
            p_card_data = result(search_keyword)
            Postcard_items = mod.objects.create(image=p_card_data[0],
                                                wiki_sentence=p_card_data[1],
                                                tweet_text=p_card_data[2].encode('utf-8')
                                                )
            Postcard = mod.objects.all()
            return render(request, 'PostcardApp/index.html', {'Postcard': Postcard})


def result(search_keyword):
    Postcard_data = []
    Pixabay_Image = get_image(search_keyword)
    Wiki_snip = get_wiki_content(search_keyword)
    tweet_txt = (get_tweet(search_keyword))
    if Pixabay_Image:
        Postcard_data.append(Pixabay_Image)
    else:
        Postcard_data.append("No image found")

    if Wiki_snip:
        Postcard_data.append(Wiki_snip)
    else:
        Postcard_data.append("No wiki snippet found")
    if tweet_txt:
        Postcard_data.append(tweet_txt) # get a tweet
    else:
        Postcard_data.append("No tweet found")

    return Postcard_data



