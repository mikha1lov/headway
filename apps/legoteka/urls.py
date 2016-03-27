from django.conf.urls import url
from views import home, legoteka_by_category

urlpatterns = [url(r'^$', home, name='home'),
               url(r'^(?P<pk>\d+)/$', legoteka_by_category, name='by_category'),]
