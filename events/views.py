from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

EVENT_SLUGS = [
    'hackathon',
    'bot-xchange',
    'quiz',
    'gaming',
    'crypt-hunt',
    'image-ination',
    'ad-making',
    'code-combat',
    'web-design',
    'pac-man',
]

def event(request, slug):
    if slug not in EVENT_SLUGS: return HttpResponseNotFound()
    template = f'events/{slug}.html'
    return render(request, template)

def schedule(request):
    return render(request, 'schedule.html')
    # return HttpResponseRedirect('/static/ShriTeq2022_Schedule.pdf')