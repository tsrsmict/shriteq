from django.urls import path
from django.views.generic import TemplateView
from http import HTTPStatus
from django.conf import settings
from django.shortcuts import HttpResponse, render

def teapot(request):
    return HttpResponse("for real", status=HTTPStatus.IM_A_TEAPOT)

urlpatterns = [
    path('whoami', teapot, name='whoami'),
]

