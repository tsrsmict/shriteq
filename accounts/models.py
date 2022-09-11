from django.db import models

from django.conf import settings

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    ch_level = models.SmallIntegerField()
    date_modified = models.DateTimeField(auto_now=True)