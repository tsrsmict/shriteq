from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pac_man/index.html')

def leaderboard(request):
    context = {}
    return render(request,'pac_man/leaderboard.html', context=context)

def play(request):
    context = {}
    return render(request, 'pac_man/play.html', context=context)