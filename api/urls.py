# -*- coding: utf-8 -*-
from django.conf.urls import url

import views as api_views


urlpatterns = [
    url(r'^feedback/new/$', api_views.create_feedback),
    url(r'^books/$', api_views.books),
]
