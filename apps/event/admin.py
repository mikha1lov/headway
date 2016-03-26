# coding: utf-8
from django.contrib import admin

from models import Event, EventType, EventParticipants

admin.site.register(Event, admin.ModelAdmin)
admin.site.register(EventType, admin.ModelAdmin)
admin.site.register(EventParticipants, admin.ModelAdmin)
