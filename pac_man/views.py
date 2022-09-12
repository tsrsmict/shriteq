from django.shortcuts import render
from django.views.generic import View
from events.views import BaseOnlineEventView

# Create your views here.
class Index(BaseOnlineEventView):
    def get(self, request):
        return render(request, 'pac_man/index.html')

class Leaderboard(BaseOnlineEventView):
    def get(self, request):
        context = {}
        return render(request,'pac_man/leaderboard.html', context=context)

class Play(BaseOnlineEventView):
    def get(self, request):
        context = {}
        return render(request, template_name='pac_man/play.html', context=context)
    def post(self, request):
        pass