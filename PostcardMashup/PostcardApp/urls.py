from django.contrib import admin
app_name = 'PostcardApp'

from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # url('^$', TemplateView.as_view(template_name='index.html')),
]