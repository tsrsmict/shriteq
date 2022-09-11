from django.db import models
import uuid

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    serial_num = models.SmallIntegerField()
    question = models.TextField()
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