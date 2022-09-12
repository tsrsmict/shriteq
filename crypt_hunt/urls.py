import datetime

from django.urls import path
from django.views.generic import TemplateView

from django.conf import settings
from . import views

urlpatterns = []


if settings.OPEN_EVENTS_RUNNING:
    urlpatterns += [
        path('', views.index, name='crypt_hunt_index'),
        path('rules', TemplateView.as_view(template_name='crypt_hunt/rules.html'), name='crypt_hunt_rules'),
        path('leaderboard', views.leaderboard, name='crypt_hunt_leaderboard'),
        path('play', views.Play.as_view(), name='crypt_hunt_play'),
        path('congrats', views.congrats, name='crypt_hunt_congrats'),
    ]
else: 
    urlpatterns += [
        path('', TemplateView.as_view(template_name='crypt_hunt/waiting.html'), name='crypt_hunt_waiting'),
    ]