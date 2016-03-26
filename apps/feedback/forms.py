# coding: utf-8
from django.forms import ModelForm

from models import Feedback


class NewFeedBackForm(ModelForm):

    class Meta:
        model = Feedback
        exclude = ()
