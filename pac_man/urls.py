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
        path('play/', views.Play.as_view(), name='pac_man_play'),
    ]
else: 
    urlpatterns += [
        path('', TemplateView.as_view(template_name='pac_man/waiting.html'), name='pac_man_waiting'),
    ]