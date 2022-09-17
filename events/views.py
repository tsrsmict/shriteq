from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
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
    return render(request, 'schedule.html')
    # return HttpResponseRedirect('/static/ShriTeq2022_Schedule.pdf')

def open_events(request):
    if not request.user.is_authenticated: return HttpResponseRedirect('/accounts/login')
    context = {}

    school = School.objects.get(account=request.user)
    context['school'] = school

    session = request.session
    context['user_id'] = session['user_id']

    return render(request, 'open-events.html', context)


class BaseOnlineEventView(generic.View):
    def check_auth(self, request) -> bool:
        print('Check auth called')
        is_auth = request.user.is_authenticated
        print(f'{is_auth=}')
        return is_auth