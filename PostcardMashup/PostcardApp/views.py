from django.shortcuts import render
from . models import API_model as mod
from APItools.API_Manager import get_image, get_tweet, get_wiki_content
import sys, os
# Create your views here.
# sys.path.append(r"/Users/chitrakakkar/PycharmProjects/Capstone_FinalProject")
# os.environ['PATH'] = (r" /Users/chitrakakkar/PycharmProjects/Capstone_FinalProject;"
#                       + os.environ['PATH'])


def index(request):
    # The `POST` has the data from the HTML form that was submitted.
    # ORM queries the database for all of the to-do entries.
    if request.method == 'GET':
        return render(request, 'PostcardApp/index.html')
    elif request.method == 'POST':
            search_keyword = request.POST.get('search')
            Postcard_items = mod.objects.create(image=result(search_keyword)[0],
                                                wiki_sentence=result(search_keyword)[1],
                                                tweet_text=result(search_keyword)[2])
            Postcard = mod.objects.all()
            return render(request, 'PostcardApp/index.html', {'Postcard': Postcard})


# def result_page(request):
#     if request.method == 'POST':
#         search_keyword = request.POST.get('search')
#         Postcard_items = mod.objects.create(image=result(search_keyword)[0], wiki_sentence=result(search_keyword)[1], tweet_text=result(search_keyword)[2])
#         Postcard = mod.objects.all()
#         return render(request, 'PostcardApp/index.html', {'Postcard': Postcard})


def result(search_keyword):
    Postcard_data = []
    Pixabay_Image = get_image(search_keyword)
    Wiki_snip = get_wiki_content(search_keyword)
    tweet_txt = (get_tweet(search_keyword))
    Postcard_data.append(Pixabay_Image)
    Postcard_data.append(Wiki_snip)
    Postcard_data.append(tweet_txt)
    return Postcard_data



