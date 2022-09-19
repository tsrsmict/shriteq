from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.templatetags.static import static

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
    if slug not in EVENT_SLUGS: return HttpResponseNotFound(render(request, '404.html'))
    template = f'events/{slug}.html'
    return render(request, template)

def schedule(request):
    return redirect('/static/ShriTeq2022_Schedule.pdf')