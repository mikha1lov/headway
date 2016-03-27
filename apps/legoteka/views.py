from django.shortcuts import render
from .models import LegotekaItem, Category


def home(request):
    categories = Category.objects.all()
    items = LegotekaItem.objects.all()
    return render(request, 'legoteka.html', locals())


def legoteka_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    categories = Category.objects.all()
    items = LegotekaItem.objects.filter(category=category)
    print(items)
    return render(request, 'legoteka.html', locals())
