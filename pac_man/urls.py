import datetime

from django.urls import path
from django.views.generic import TemplateView

from django.conf import settings
from . import views

urlpatterns = []


now = datetime.datetime.now(tz=settings.TIME_ZONE_INFO)
if settings.DEBUG == True or now >= settings.OPEN_EVENT_START_TIME:
    urlpatterns += [
        path('', views.index, name='pac_man_index'),
        path('rules', TemplateView.as_view(template_name='pac_man/rules.html'), name='pac_man_rules'),
        path('leaderboard', views.leaderboard, name='pac_man_leaderboard'),
        path('play', views.play, name='pac_man_play'),
    ]
else: 
    urlpatterns += [
        path('', TemplateView.as_view(template_name='pac_man/waiting.html'), name='pac_man_waiting'),
    ]