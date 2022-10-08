from django.contrib import admin
from .models import Question, Submission

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('serial_num', 'question', 'answer')
    ordering = ('serial_num',)

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('question_num', 'contents', 'status', 'time', 'school', 'user_id', 'ip_address')
    search_fields = ('question_num', 'contents', 'status', 'time', 'school', 'user_id', 'ip_address')