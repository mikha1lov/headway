# coding: utf-8
from django.forms import ModelForm
from redactor.widgets import RedactorEditor

from models import Page


class PageAdminForm(ModelForm):
    class Meta:
        model = Page
        exclude = ()
        widgets = {
           'content': RedactorEditor(),
        }
