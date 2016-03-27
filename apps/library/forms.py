# coding: utf-8
from django import forms

from models import BookOrder


class BookOrderForm(forms.ModelForm):
    class Meta:
        model = BookOrder
        exclude = ()
        widgets = {
            'name': forms.TextInput(attrs={'class':'form_name', 'placeholder':u'ФИО'}),
            'contacts': forms.TextInput(attrs={'class':'form_contacts', 'placeholder':u'E-mail или телефон'}),
            'note': forms.Textarea(attrs={'class':'form_note', 'placeholder':u'Комментарий'}),
        }
