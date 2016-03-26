# coding: utf-8
from django.contrib import admin
from models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts', 'created')


admin.site.register(Feedback, FeedbackAdmin)
