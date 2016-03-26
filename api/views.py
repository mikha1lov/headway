# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from apps.feedback.forms import NewFeedBackForm
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
