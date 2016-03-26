from django.http import Http404
from django.shortcuts import render
from models import Page


def pages_detail(request, page):
    try:
        page = Page.objects.get(url=page)
    except:
        raise Http404

    return render(request, "pages/page_detail.html", {'page': page})