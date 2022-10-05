import datetime

from django.urls import path
from django.views.generic import TemplateView

from django.conf import settings
from . import views

urlpatterns = []

if settings.OPEN_EVENTS_RUNNING:
    urlpatterns += [
        path('', views.Index.as_view(), name='pac_man_index'),
        path('rules', TemplateView.as_view(template_name='pac_man/rules.html'), name='pac_man_rules'),
        path('leaderboard', views.Leaderboard.as_view(), name='pac_man_leaderboard'),
        path('play', views.Play.as_view(), name='pac_man_play'),
    ]
else: 
    if settings.IS_IN_EVENT_WINDOW:
        # Is in general event window but at a closed time, (not 3pm-11:59 pm on weekdays and not 9:00 am - 11:59 pm on weekends)
        urlpatterns += [
            path('', views.GetSomeSleep.as_view(), name='crypt_hunt_sleep'),
        ]
    else:
        urlpatterns += [
            path('', TemplateView.as_view(template_name='crypt_hunt/waiting.html'), name='crypt_hunt_waiting'),
        ]