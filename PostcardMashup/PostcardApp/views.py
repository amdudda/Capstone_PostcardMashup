from django.shortcuts import render
from . models import API_model as models
# Create your views here.


def index(request):
    # The `POST` has the data from the HTML form that was submitted.
    # ORM queries the database for all of the to-do entries.
    if request.method == 'POST':
        # Get the data from the form
        sentence = request.POST.get('sentence')
        description = request.POST.get('description')
        # add the data to the database
        # items = models.objects.create(sentence=, search_term=description, saved_on=)

    # Gets the todos we need from the database
    items = models.objects.all()
    # render the page with the todos list
    return render(request, 'MytodoListApp/index.html', {'items': items})