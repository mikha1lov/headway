from django.shortcuts import render
from django.utils import timezone

from apps.base.models import News
from apps.event.models import Event


def home(request):
    slider_events = Event.objects.filter(data__lt=timezone.now())
    events = Event.objects.filter(data__gte=timezone.now())
    news = News.objects.all()[:10]
    return render(request, 'base/home.html', locals())
