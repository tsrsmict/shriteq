from datetime import datetime
import os
import pathlib
import csv

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import django.views.generic as generic

from accounts.models import School
from .models import Question, Submission
from events.views import BaseOnlineEventView
from events.utils import download_csv

from django.conf import settings
User = settings.AUTH_USER_MODEL

# NUM_QUESTIONS = Question.objects.count()
# Load as newline-separated from BANNED_IPS.TXT

base_path = pathlib.Path().resolve()

f = open(os.path.join(base_path, 'crypt_hunt', 'banned_ips.txt'), 'r')
banned_ips = f.read().splitlines()


class BaseCryptHuntView(BaseOnlineEventView):
    def is_allowed(self, request) -> bool:
        return super().is_authenticated(request) and not School.objects.get(account=request.user).is_ch_banned

class Index(BaseCryptHuntView):
    def get(self, request):
        if not super().is_allowed(request): return redirect('open')
        return redirect(reverse('crypt_hunt_play'))

class Leaderboard(BaseCryptHuntView):
    def get(self, request):
        if not super().is_allowed(request): return redirect(reverse('open'))
        schools = School.objects.all().order_by('-question_num', 'ch_levelup_time')

        context = {'schools': schools}
        return render(request,'crypt_hunt/leaderboard.html', context=context)

class Congrats(BaseCryptHuntView):
    def get(self, request):
        if not super().is_allowed(request): return redirect(reverse('open'))
        school = School.objects.get(account=request.user)
        if not school.question:
            return render(request, 'crypt_hunt/congrats.html')
        else:
            return redirect('crypt_hunt_play')

class Play(BaseCryptHuntView):
    def get(self, request):
        if not super().is_allowed(request): return redirect(reverse('open'))
        context = {}
        try:
            school = School.objects.get(account=request.user)
            question = school.question
            context['question'] = question
            context['school'] = school

            session = request.session
            context['user_id'] = session['user_id']
            
        except Exception as e:
            print(f'{e=} {type(e)=}')
            return redirect('open')
        
        if school.question == None:
            return redirect('crypt_hunt_congrats')
        return render(request, template_name='crypt_hunt/play.html', context=context)

    def post(self, request):
        if not super().is_allowed(request): return redirect(reverse('open'))
        data = (request.POST)
        session = request.session
        
        try:
            # Check if the hidden input was deleted / something's been corrupted / attempt to hack
            current_question_num = int(data['question-num'])
        except:
            # Reload
            return self.get(request)

        contents = data['answer']

        # Shdowban
        ip = get_client_ip(request)
        if ip in banned_ips:
            return redirect(reverse('crypt_hunt_play'))
        
        log = {
            'contents': contents,
            'ip_address': get_client_ip(request),
            'time': str(datetime.now())
        }

        try:
            user_id = session['user_id']
            school = School.objects.get(account=request.user)
            question = school.question
        except:
            return self.get(request)

        # Make sure that this isn't being submitted from someone who hasn't reloaded since the school progressed
        if question is not None and question.serial_num == current_question_num:
            # Validate the submission with an advanced function
            if submission_correct(contents, question):
                # Advance the question
                school.question_num += 1
                school.ch_levelup_time = datetime.now()
                school.save()
                log['status'] = 'COR'
            else:
                log['status'] = 'INC'
        else: 
            log['status'] = 'ODT'            

        log['user_id'] = user_id
        log['school'] = str(school)
        log['question_num'] = current_question_num
        
        save_log(log)
        return redirect(reverse('crypt_hunt_play'))


class GetSomeSleep(BaseCryptHuntView):
    def get(self, request):
        if not super().is_allowed(request): return redirect(reverse('open'))
        context = {}
        if settings.IS_WEEKEND: 
            context['resume_time'] = '9:00 AM tomorrow'
        else:
            context['resume_time'] = '3:00 PM'
        return render(request, 'crypt_hunt/get-some-sleep.html', context=context)
        

def logs_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    data = download_csv(request, Submission.objects.all())
    response = HttpResponse(data, content_type='text/csv')
    return response

# Utils
def submission_correct(answer: str, question: Question) -> bool:
    return answer.lower().strip().replace(' ', '') == question.answer.lower().strip().replace(' ', '')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def save_log(log: dict):
    Submission.objects.create(**log)