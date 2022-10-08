import uuid

from django.db import models
from django.templatetags.static import static

from ckeditor.fields import RichTextField

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    serial_num = models.SmallIntegerField()
    question = RichTextField(default=None, blank=True, null=True)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.serial_num}: {self.question}'
    
    @property
    def next_question(self):
        try:
            question = Question.objects.get(serial_num=self.serial_num + 1)
            return question
        except:
            return None

    """
    TODO: This is a workaround to get around Heroku's ephermal file system. Ideally, we
    should use a proper service like S3 to host our files and use django-ckeditor's 
    RichTextUplodingField to dynamically upload files to questions without having to host 
    them as staticfiles.
    """
    image_paths_list = models.TextField(default=None, null=True, blank=True)
    @property
    def static_image_paths(self):
        if self.image_paths_list is None or len(self.image_paths_list.strip()) == 0 and self.image_paths_list == '':
            return []
        paths = [static(path) for path in self.image_paths_list.split('\n')]
        return paths

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
