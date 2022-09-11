import datetime

from django.urls import path
from django.views.generic import TemplateView

from django.conf import settings
from . import views

urlpatterns = []


now = datetime.datetime.now(tz=settings.TIME_ZONE_INFO)
if settings.DEBUG == True or now >= settings.OPEN_EVENT_START_TIME:
    urlpatterns += [
        path('', views.index, name='crypt_hunt_index'),
        path('rules', TemplateView.as_view(template_name='crypt_hunt/rules.html'), name='crypt_hunt_rules'),
        path('leaderboard', views.leaderboard, name='crypt_hunt_leaderboard'),
        path('play', views.play, name='crypt_hunt_play'),
    ]
else: 
    urlpatterns += [
        path('', TemplateView.as_view(template_name='crypt_hunt/waiting.html'), name='crypt_hunt_waiting'),
    ]