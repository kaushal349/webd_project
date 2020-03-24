from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length = 30)
    option2 = models.CharField(max_length = 30)
    option3 = models.CharField(max_length = 30)
    option1count = models.IntegerField(default=0)
    option2count = models.IntegerField(default=0)
    option3count = models.IntegerField(default=0)
