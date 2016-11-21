from django.db import models
import datetime


# Create your models here.


class API_model(models.Model):
    sentence = models.CharField(max_length=300, null=False)
    search_term = models.CharField(max_length=100, null=False, unique=True)
    saved_on = models.DateTimeField(null=False, default=datetime.datetime)



