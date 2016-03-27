# coding: utf-8
from django.shortcuts import render

from apps.financial.forms import FinancialEventParticipantsForm
from models import FinancialEvent


def financial_event_list(request):
    message = None
    financial_events = FinancialEvent.objects.all().order_by('date')
    event_take_part_form = FinancialEventParticipantsForm(request.POST or None, request.GET or None)
    if request.method == 'POST':
        if event_take_part_form.is_valid():
            new_request = event_take_part_form.save(commit=False)
            new_request.event = request.GET['financial_event_id']
            new_request.save()
            message = 'Запрос отправлен'

    return render(request, 'financial_event.html', {'financial_events': financial_events, 'event_take_part_form': event_take_part_form, 'message': message})
