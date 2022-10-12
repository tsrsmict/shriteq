import csv

from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views import View
import django.views.generic as generic
from django.conf import settings

from accounts.models import School
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

def open_events(request):
    if not request.user.is_authenticated: return redirect('login')
    context = {}

    school = School.objects.get(account=request.user)
    context['school'] = school
    session = request.session
    context['user_id'] = session['user_id']

    if school.is_ch_banned:
        context['is_ch_banned'] = True
    if school.is_pac_banned:
        context['is_pac_banned'] = True

    return render(request, 'open-events.html', context)

class GetSomeSleep(View):
    def get(self, request):
        context = {}
        if settings.IS_WEEKEND: 
            context['resume_time'] = '9:00 AM tomorrow'
        else:
            context['resume_time'] = '3:00 PM'
        return render(request, 'get-some-sleep.html', context=context)

class BaseOnlineEventView(generic.View):
    def is_authenticated(self, request) -> bool:
        is_auth = request.user.is_authenticated
        return is_auth

  