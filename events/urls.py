from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from django.conf import settings
from . import views 

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('events/<str:slug>/', views.event, name='event'),
    path('schedule', views.schedule, name='schedule'),
    path('rules', TemplateView.as_view(template_name='rules.html'), name='rules'),
]

if settings.OPEN_EVENTS_RUNNING:
    urlpatterns += path('open/', views.open_events, name='open'),