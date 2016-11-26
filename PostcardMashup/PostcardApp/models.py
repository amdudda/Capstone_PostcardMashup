from django.db import models
import datetime


# Create your models here.

class API_model(models.Model):
    image = models.CharField(max_length=300, null=False)
    wiki_sentence = models.CharField(max_length=100, null=False, unique=False)
    tweet_text = models.CharField(max_length=100, null=False, unique=False)
    Saved_n = models.DateTimeField(null=False, auto_now=True)#default=datetime.datetime)
    search_string = models.CharField(max_length=100, blank=True) # just in case someone gets cute and tries to pass an empty string



