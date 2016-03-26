from django.conf.urls import url

from base.views import home

urlpatterns = [url(r'^$', home, name='home'),]