# coding: utf-8
from django import forms

from models import BookOrder


class BookOrderForm(forms.ModelForm):
    class Meta:
        model = BookOrder
        exclude = ('item', )
