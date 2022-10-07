from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
import django.views.generic as generic

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


class BaseOnlineEventView(generic.View):
    def is_authenticated(self, request) -> bool:
        is_auth = request.user.is_authenticated
        return is_auth
