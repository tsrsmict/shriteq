from django.db import models
import uuid
from ckeditor.fields import RichTextField

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    serial_num = models.SmallIntegerField()
    question = RichTextField()
    answer = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.serial_num}: {self.question}'
    
    @property
    def next_question(self):
        try:
            question = Question.objects.get(serial_num=self.serial_num + 1)
            print(question)
            return question
        except:
            return None

class Submission(models.Model):
    question_num = models.IntegerField(default=0)
    contents = models.CharField(max_length=1000)

    STATUS_CHOICES = [
        ('ODT', 'Outdated'),
        ('COR', 'Correct'),
        ('INC', 'Incorrect')
    ]
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='INC')

    # Metadata
    time = models.DateTimeField(auto_now_add=True)
    school = models.CharField(max_length=100) # to prevent recursive import hell
    user_id = models.CharField(max_length=100, default=None, null=True)
    ip_address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.question_num}: {self.contents} ({self.user_id} {self.school})'