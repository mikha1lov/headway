# coding: utf-8
from django import forms

from apps.base.models import Follower


class NewFollowerForm(forms.ModelForm):
    class Meta:
        model = Follower
        exclude = ()
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form_email', 'placeholder': u'Ваш E-mail'}),
        }
