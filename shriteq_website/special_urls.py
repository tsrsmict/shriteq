from django.urls import path
from http import HTTPStatus
from django.shortcuts import HttpResponse


# For crypt hunt question
def teapot(request):
    return HttpResponse("for real", status=HTTPStatus.IM_A_TEAPOT)

urlpatterns = [
    path('whoami', teapot, name='whoami'),
]

