from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

EVENT_SLUGS = [
    'hackathon',
    'bot-trading',
    'senior-quiz',
    'middle-quiz',
    'junior-quiz',
    'crypt-hunt',
    'competitive-gaming',
    'photoshop-battles',
    'ad-making',
    'programming',
    'drone-racing',
    'web-design',
    'pac-man',
]

def event(request, slug):
    if slug not in EVENT_SLUGS: return HttpResponseNotFound()
    template = f'events/{slug}.html'
    return render(request, template)