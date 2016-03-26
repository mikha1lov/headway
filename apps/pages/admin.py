# -*- coding: utf-8 -*-
from django.contrib import admin

from forms import PageAdminForm
from models import Page


class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm
    list_display = ('title', 'url')
    prepopulated_fields = {"url": ("title",)}


admin.site.register(Page, PageAdmin)
