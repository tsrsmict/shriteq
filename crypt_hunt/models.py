from django.db import models
from accounts.models import School
import uuid

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    serial_number = models.SmallIntegerField()
    question = models.TextField()
    answer = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.serial_number}: {self.question}'