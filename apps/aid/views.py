from django.shortcuts import render

from apps.aid.models import HumanitarianAid


def humanitarian_aid(request):
    items = HumanitarianAid.objects.all()
    return render(request, 'humanitarian_aid.html', locals())
