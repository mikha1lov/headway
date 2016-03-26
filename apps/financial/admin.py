from django.contrib import admin

from models import FinancialEvent, FinancialEventParticipants

admin.site.register(FinancialEvent, admin.ModelAdmin)
admin.site.register(FinancialEventParticipants, admin.ModelAdmin)