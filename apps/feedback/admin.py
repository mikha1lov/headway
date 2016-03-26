# coding: utf-8
from django.contrib import admin

from models import Feedback

admin.site.register(Feedback, admin.ModelAdmin)