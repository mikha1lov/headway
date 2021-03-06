# coding: utf-8

from django import forms
from apps.legoteka.models import LegotekaItemOrder


class LegotekaOrderForm(forms.ModelForm):
    class Meta:
        model = LegotekaItemOrder
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form_name', 'placeholder': u'ФИО', 'required': 'True'}),
            'contacts': forms.TextInput(attrs={'class': 'form_contacts', 'placeholder': u'E-mail или телефон',
                                               'required': 'True'}),
            'note': forms.Textarea(attrs={'class': 'form_note', 'placeholder': u'Комментарий', 'required': 'True'}),
        }
