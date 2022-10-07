from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.models import School
from .models import PacManPlayer
from events.views import BaseOnlineEventView
from django.shortcuts import render

from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your views here.
class Index(BaseOnlineEventView):
    def get(self, request):
        if not super().is_authenticated(request): return redirect('open')
        return redirect(reverse('pac_man_play'))

class Leaderboard(BaseOnlineEventView):
    def get(self, request):
        players = PacManPlayer.objects.order_by('-high_score')[:10]
        players = [player for player in players if player.high_score != 0]
        context = {'players': players}
        return render(request,'pac_man/leaderboard.html', context=context)

class Play(BaseOnlineEventView):
    def get(self, request):
        if not super().is_authenticated(request): return redirect('open')
        context = {}
        try:
            school = School.objects.get(account=request.user)
            context['school'] = school
        except Exception as e:
            print(f'{e=} {type(e)=}')
            return redirect('open')
        
        try:
            session = request.session
            user_id = session['user_id']
            query = PacManPlayer.objects.filter(user_id=user_id)
            if len(query) == 0:
                player = PacManPlayer(user_id=user_id, school=school)
                player.save()
            else:
                player = query[0]
            context['player'] = player
        except Exception as e:
            print(f'{e=} {type(e)=}')
            return redirect('open')

        return render(request, template_name='pac_man/play.html', context=context)
    def post(self, request, *args, **kwargs):
        if not super().is_authenticated(request): return redirect('open')
        
        data = request.POST
        game_score = int(data['game-score-input'])
        user_id = data['user-id']

        try:
            school = School.objects.get(account=request.user)
            player = PacManPlayer.objects.get(user_id=user_id, school=school)
        except Exception as e:
            print(f'{e=} {type(e)=}')
            return redirect('open')

        if player.high_score < game_score:
            player.high_score = game_score
            player.save()
        else:
            pass
        return HttpResponse('Received')

class GetSomeSleep(BaseOnlineEventView):
    def get(self, request):
        if not super().is_authenticated(request): return redirect('open')
        context = {}
        if settings.IS_WEEKEND: 
            context['resume_time'] = '9:00 AM tomorrow'
        else:
            context['resume_time'] = '3:00 PM'
        return render(request, 'get-some-sleep.html', context=context)