import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.utils import timezone

from apps.base.models import News
from apps.event.models import Event


def home(request):
    slider_events = Event.objects.filter(date__lt=timezone.now())
    events = Event.objects.filter(date__gte=timezone.now()).values('title', 'date', 'type')
    print(events)
    events = json.dumps(list(events), cls=DjangoJSONEncoder)
    print(events)
    news = News.objects.all()[:10]
    return render(request, 'base/home.html', locals())
