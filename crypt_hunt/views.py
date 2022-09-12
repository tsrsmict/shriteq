from datetime import datetime
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse

from accounts.models import School
from .models import Question

from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your views here.
def index(request):
    return render(request, 'crypt_hunt/index.html')

def leaderboard(request):
    schools = School.objects.all().order_by('-question__serial_num', 'date_modified')

    context = {'schools': schools}
    return render(request,'crypt_hunt/leaderboard.html', context=context)

def congrats(request):
    school = School.objects.get(account=request.user)
    if school.question.serial_num == Question.objects.last().serial_num + 1:
        return render(request, 'crypt_hunt/congrats.html')
    else:
        return HttpResponseRedirect(reverse('crypt_hunt_play'))

class Play(View):
    def get(self, request):
        context = {}
        try:
            print(request.user)
            school = School.objects.get(account=request.user)
            question = school.question
            context['question'] = question
            context['school'] = school

            session = request.session
            context['user_id'] = session['user_id']
            
        except Exception as e:
            print(e)
            return HttpResponseRedirect(reverse('crypt_hunt_index'))
        if school.question == None:
            return HttpResponseRedirect(reverse('crypt_hunt_congrats'))
        return render(request, template_name='crypt_hunt/play.html', context=context)

    def post(self, request):
        data = (request.POST)
        session = request.session
        
        try:
            # Check if the hidden input was deleted / something's been corrupted / attempt to hack
            current_question_num = int(data['question-num'])
        except:
            # Reload
            return self.get(request)

        answer = data['answer']
        log = {
            'answer': answer,
            'ip': get_client_ip(request),
            'time': datetime.now()
        }

        try:
            user_id = session['user_id']
            school = School.objects.get(account=request.user)
            question = school.question
        except:
            print('Missing credentials in session')
            return self.get(request)

        # Make sure that this isn't being submitted from someone who hasn't reloaded since the school progressed
        if question.serial_num == current_question_num:
            # Validate the submission with an advanced function
            if submission_correct(answer, question):
                # Advance the question
                school.question = question.next_question
                school.save()
                log['correct'] = True
            else:
                log['correct'] = False

        log['user_id'] = user_id
        log['school'] = school
        log['question_num'] = question.serial_num

        save_log(log)
        return self.get(request)


# Utils
def submission_correct(answer: str, question: Question) -> bool:
    return answer.lower().strip() == question.answer.lower().strip()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def save_log(log: dict):
    print(f'{log=}')