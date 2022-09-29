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
        if not super().check_auth(request): return redirect('open')
        return redirect(reverse('pac_man_play'))

class Leaderboard(BaseOnlineEventView):
    def get(self, request):
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
    def post(self, request, *args, **kwargs):
        if not super().check_auth(request): return redirect('open')
        
        data = request.POST
        print(data)
        game_score = int(data['game-score-input'])
        user_id = data['user-id']

        try:
            print(request.user)
            school = School.objects.get(account=request.user)
            player = PacManPlayer.objects.get(user_id=user_id, school=school)
        except Exception as e:
            print(f'{e=} {type(e)=}')
            return HttpResponseRedirect(reverse('open'))

        print(f'Found  player {player} of school {school}')
        if player.high_score < game_score:
            print(f'Updating high score from {player.high_score} to {game_score}')
            player.high_score = game_score
            player.save()
        else:
            print(f'Score {game_score} less than high score {player.high_score}')

        print('Received post')
        return HttpResponse('Received')

class GetSomeSleep(BaseOnlineEventView):
    def get(self, request):
        if not super().check_auth(request): return redirect('open')
        context = {}
        if settings.IS_WEEKEND: 
            context['resume_time'] = '9:00 AM tomorrow'
        else:
            context['resume_time'] = '3:00 PM'
        return render(request, 'get-some-sleep.html', context=context)