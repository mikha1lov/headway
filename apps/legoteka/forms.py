from django import forms
from apps.legoteka.models import LegotekaItemOrder


class LegotekaOrderForm(forms.ModelForm):
    class Meta:
        model = LegotekaItemOrder
        fields = '__all__'
