from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

from .list import EVENTS_LIST

# Create your views here.
def event(request, slug):
    matching_event = EVENTS_LIST.get(slug, None)
    if not matching_event: return HttpResponse('Event not found', status=404)
    template = f'events/{slug}.html'
    return render(request, template, {'event': matching_event})