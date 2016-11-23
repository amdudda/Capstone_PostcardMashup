from django.contrib import admin
app_name = 'PostcardApp'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),

    # url('^$', TemplateView.as_view(template_name='index.html')),
]