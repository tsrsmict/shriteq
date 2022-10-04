from django.db import models
from accounts.models import School

# Create your models here.
class PacManPlayer(models.Model):
    user_id = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
    num_attempts = models.IntegerField(default=0, editable=False)
    high_score = models.IntegerField(default=0)
    last_played = models.DateTimeField(auto_now=True)

    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_id} - {self.school} - {self.high_score}'
    
    def __save__(self, *args, **kwargs):
        self.num_attempts += 1
        super().__save__(*args, **kwargs)