import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.utils import timezone

from apps.base.models import News
from apps.event.models import Event
from apps.base.forms import NewFollowerForm


def home(request):
    slider_events = Event.objects.all()
    events = Event.objects.all().values('id', 'title', 'date', 'type')
    print(events)
    events = json.dumps(list(events), cls=DjangoJSONEncoder)
    print(events)
    news = News.objects.all()[:10]
    folow_form = NewFollowerForm(request.POST or None)
    if folow_form.is_valid():
        folow_form.save()
    return render(request, 'base/home.html', locals())
