from django.db import models
from django.conf import settings
from crypt_hunt.models import Question

class School(models.Model):
    display_name = models.CharField(max_length=100)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)
    
    # Setting the default question to the first question in the database.
    question_num = models.SmallIntegerField(default=1, null=True)
    date_modified = models.DateTimeField(auto_now=True)

    is_ch_banned = models.BooleanField(default=False)
    is_pac_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.account.username

    @property
    def question(self):
        return Question.objects.filter(serial_num=self.question_num).first()