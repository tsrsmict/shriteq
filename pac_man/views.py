from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.models import School
from .models import PacManPlayer
from events.views import BaseOnlineEventView

from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your views here.
class Index(BaseOnlineEventView):
    def get(self, request):
        return render(request, 'pac_man/index.html')

class Leaderboard(BaseOnlineEventView):
    def get(self, request):
        # Top 10 players by highscore
        players = PacManPlayer.objects.order_by('-high_score')[:10]
        players = [player for player in players if player.high_score != 0]
        context = {'players': players}
        return render(request,'pac_man/leaderboard.html', context=context)

class Play(BaseOnlineEventView):
    def get(self, request):
        if not super().check_auth(request): return redirect('open')
        context = {}
        try:
            print(request.user)
            school = School.objects.get(account=request.user)
            context['school'] = school
        except Exception as e:
            print(f'{e=} {type(e)=}')
            return HttpResponseRedirect(reverse('open'))
        
        try:
            session = request.session
            user_id = session['user_id']
            print(user_id)
            query = PacManPlayer.objects.filter(user_id=user_id)
            if len(query) == 0:
                player = PacManPlayer(user_id=user_id, school=school)
                player.save()
            else:
                player = query[0]
            print(player.user_id)
            context['player'] = player
        except Exception as e:
            print(f'{e=} {type(e)=}')
            return HttpResponseRedirect(reverse('open'))

        return render(request, template_name='pac_man/play.html', context=context)
    def post(self, request):
        pass