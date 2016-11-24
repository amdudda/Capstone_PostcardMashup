from django.contrib import admin
app_name = 'PostcardApp'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    # url(r'^$', views.result_page, name='result_page')
]
