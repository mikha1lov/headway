from django.shortcuts import render

from apps.aid.models import HumanitarianAidForKid, HumanitarianAidForSponsors


def humanitarian_aid(request):
    for_kids = HumanitarianAidForKid.objects.all()
    for_sponsors = HumanitarianAidForSponsors.objects.all()
    return render(request, 'humanitarian_aid.html', locals())
