# coding: utf-8
from django.contrib import admin

from models import HumanitarianAid, AidType, AidRequest, GivingAid

admin.site.register(HumanitarianAid, admin.ModelAdmin)
admin.site.register(AidType, admin.ModelAdmin)
admin.site.register(AidRequest, admin.ModelAdmin)
admin.site.register(GivingAid, admin.ModelAdmin)
