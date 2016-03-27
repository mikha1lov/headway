from django.conf.urls import url
from views import financial_event_list

urlpatterns = [url(r'^$', financial_event_list, name='home'), ]

