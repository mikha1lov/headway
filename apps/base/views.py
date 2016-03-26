import json
from django.shortcuts import render
from django.utils import timezone

from django.core import serializers
from apps.base.models import News
from apps.event.models import Event


def home(request):
    slider_events = Event.objects.filter(data__lt=timezone.now())
    events = Event.objects.filter(data__gte=timezone.now())
    news = News.objects.all()[:10]
    clndr_events = serializers.serialize("json", events, indent=2, use_natural_foreign_keys=True,
                                         use_natural_primary_keys=True, fields=('title', 'data'))
    print(clndr_events)
    return render(request, 'base/home.html', locals())
