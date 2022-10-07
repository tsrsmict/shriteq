import os
import pathlib

from django.urls import path
from http import HTTPStatus
from django.shortcuts import HttpResponse
from django.http import FileResponse

base_path = pathlib.Path().resolve()

# For crypt hunt question
def teapot(request):
    return HttpResponse("For real(er)", status=HTTPStatus.IM_A_TEAPOT)

def nvidia_logo(request):
    return FileResponse(open(os.path.join(base_path, 'media', 'nvidia_logo.png'), 'rb'))

def tv(request):
    return FileResponse(open(os.path.join(base_path, 'media', 'iCXGZHRgaN.png'), 'rb'))

def tv_pro(request):
    return FileResponse(open(os.path.join(base_path, 'media', 'iCXGZHRgaN.png'), 'rb'))

def remote(request):
    return FileResponse(open(os.path.join(base_path, 'media', 'iCXGZHRgaN.png'), 'rb'))

def controller(request):
    return FileResponse(open(os.path.join(base_path, 'media', 'iCXGZHRgaN.png'), 'rb'))

def stand(request):
    return FileResponse(open(os.path.join(base_path, 'media', 'iCXGZHRgaN.png'), 'rb'))

urlpatterns = [
    path('whoami', teapot, name='whoami'),
    path('nvidia', nvidia_logo, name='nvidia'),
]

