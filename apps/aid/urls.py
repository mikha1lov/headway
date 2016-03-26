from django.conf.urls import url
from views import humanitarian_aid

urlpatterns = [url(r'^$', humanitarian_aid, name='home'), ]

