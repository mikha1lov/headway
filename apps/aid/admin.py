# coding: utf-8
from django.contrib import admin

from models import HumanitarianAidForKid, HumanitarianAidForSponsors, AidType, AidRequest, GivingAid

admin.site.register(HumanitarianAidForSponsors)
admin.site.register(HumanitarianAidForKid)
admin.site.register(AidType)
admin.site.register(AidRequest)
admin.site.register(GivingAid)
