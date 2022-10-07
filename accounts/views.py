from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib import auth
from .models import School

# Create your views here.

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated: return redirect('/')
        context = {'schools': School.objects.all()}
        return render(request, 'accounts/login.html', context)
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['school-username']
        password = request.POST['school-password']
        print(f'{username=} {password=}')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            user_id = request.POST['user-id']
            request.session['user_id'] = user_id
            return redirect('/open')
        else:
            return redirect('/accounts/login')
    
import re
def is_valid_username(username: str) -> bool:
    username = username.strip().lower().replace(" ", "")
    return bool(re.fullmatch("[A-Za-z]+\.[A-Za-z]+", username))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login')