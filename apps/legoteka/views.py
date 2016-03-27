from django.shortcuts import render
from apps.legoteka.forms import LegotekaOrderForm
from .models import LegotekaItem, Category


def home(request):
    categories = Category.objects.all()
    category = Category.objects.first()
    items = LegotekaItem.objects.filter(category=category)
    return render(request, 'legoteka.html', locals())


def legoteka_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    categories = Category.objects.all()
    items = LegotekaItem.objects.filter(category=category)
    form = LegotekaOrderForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'legoteka.html', locals())
