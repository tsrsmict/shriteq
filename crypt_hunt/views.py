from django.shortcuts import render
from django.views.generic import View

# Create your views here.
def index(request):
    return render(request, 'crypt_hunt/index.html')

def leaderboard(request):
    context = {}
    return render(request,'crypt_hunt/leaderboard.html', context=context)

class Play(View):
    def get(self, request):
        context = {}
        return render(request, template_name='crypt_hunt/play.html', context=context)
    def post(self, request):
        pass