from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .slugs import EVENT_SLUGS

def event(request, slug):
    if slug not in EVENT_SLUGS: return HttpResponseNotFound()
    template = f'events/{slug}.html'
    return render(request, template)