# -*- coding: utf-8 -*-
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from apps.feedback.forms import NewFeedBackForm
from apps.library.models import Book
from decorators import required_post_params

@csrf_exempt
@required_post_params(['name', 'contacts', 'message'])
def create_feedback(request):
    form = NewFeedBackForm(request.POST or None)
    if form.is_valid():
        feedback = form.save(commit=False)
        feedback.save()
        return JsonResponse({
                    'status': 0,
                    'message': 'Feedback was created'
                })


def books(request):
    data = serializers.serialize('json', Book.objects.all(), fields=('title', 'description'))
    return JsonResponse({"data": data})
