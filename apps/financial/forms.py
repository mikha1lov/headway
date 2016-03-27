from django import forms

from models import FinancialEventParticipants


class FinancialEventParticipantsForm(forms.ModelForm):
    class Meta:
        model = FinancialEventParticipants
        exclude = ()
