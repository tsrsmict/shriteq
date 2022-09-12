from django.db import models
from django.conf import settings
from crypt_hunt.models import Question

class School(models.Model):
    display_name = models.CharField(max_length=100)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, default=Question.objects.first(), null=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account.username