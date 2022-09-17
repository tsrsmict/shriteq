from django.shortcuts import render
from django.views.generic import View
from events.views import BaseOnlineEventView

from .models import PacManPlayer

# Create your views here.
class Index(BaseOnlineEventView):
    def get(self, request):
        return render(request, 'pac_man/index.html')

class Leaderboard(BaseOnlineEventView):
    def get(self, request):
        # Top 10 players by highscore
        context = {'players': PacManPlayer.objects.order_by('-high_score')[:10]}
        return render(request,'pac_man/leaderboard.html', context=context)

class Play(BaseOnlineEventView):
    def get(self, request):
        context = {}
        return render(request, template_name='pac_man/play.html', context=context)
    def post(self, request):
        pass