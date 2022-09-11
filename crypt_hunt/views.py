from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'crypt_hunt/index.html')

def leaderboard(request):
    context = {}
    return render(request,'crypt_hunt/leaderboard.html', context=context)

def play(request):
    context = {}
    return render(request, 'crypt_hunt/play.html', context=context)