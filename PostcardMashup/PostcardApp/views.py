from django.shortcuts import render
from . models import API_model as mod
from APItools.API_Manager import *
# Create your views here.


def index(request):
    # The `POST` has the data from the HTML form that was submitted.
    # ORM queries the database for all of the to-do entries.
    if request.method == 'POST':
        search_keyword = request.POST.get('search')
        Postcard_data = []
        Pixabay_Image = Postcard_data.append(get_image(search_keyword))
        Wiki_snip = Postcard_data.append(get_wiki_content(search_keyword))
        tweet_txt = Postcard_data.append(get_tweet(search))
        Postcard_items = mod.objects.create(image=Pixabay_Image, wiki_sentence=Wiki_snip, tweet_text=tweet_txt )
        Postcard = mod.objects.all()
        return render(request, 'PostcardApp/index.html', {'Postcard': Postcard})
    elif request.method == 'GET':
        search_keyword = request.GET.get('search')
        Postcard_data = []
        Pixabay_Image = Postcard_data.append(get_image(search_keyword))
        Wiki_snip = Postcard_data.append(get_wiki_content(search_keyword))
        tweet_txt = Postcard_data.append(get_tweet(search))
        Postcard_items = mod.objects.create(image=Pixabay_Image, wiki_sentence=Wiki_snip, tweet_text=tweet_txt)
        Postcard = mod.objects.all()
        return render(request, 'PostcardApp/index.html', {'Postcard': Postcard})




