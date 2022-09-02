from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

EVENT_SLUGS = [
    'hackathon',
    'bot-xchange',
    'quiz',
    'gaming',
    'crypt-hunt',
    'photoshop-battles',
    'ad-making',
    'programming',
    'web-design',
    'pac-man',
]

def event(request, slug):
    if slug not in EVENT_SLUGS: return HttpResponseNotFound()
    template = f'events/{slug}.html'
    return render(request, template)