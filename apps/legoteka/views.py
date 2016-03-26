from django.shortcuts import render
from .models import LegotekaItem


def home(request):
    items = LegotekaItem.objects.all().order_by('category',)
    return render(request, 'legoteka.html', locals())
