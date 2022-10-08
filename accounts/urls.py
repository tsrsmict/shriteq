import datetime

from django.urls import path
from django.views.generic import TemplateView

from django.conf import settings
from . import views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
]

if settings.OPEN_EVENTS_RUNNING:
    urlpatterns = [
        path('login/', views.login, name='login'),
    ]