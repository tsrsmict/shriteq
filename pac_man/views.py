from django.shortcuts import render
from django.views.generic import View

# Create your views here.
def index(request):
    return render(request, 'pac_man/index.html')

def leaderboard(request):
    context = {}
    return render(request,'pac_man/leaderboard.html', context=context)

class Play(View):
    def get(self, request):
        context = {}
        return render(request, template_name='pac_man/play.html', context=context)
    def post(self, request):
        pass