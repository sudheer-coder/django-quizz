from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Test(models.Model):
    question = models.CharField(max_length=7000)
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)

class Results(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    questions = models.ForeignKey(Test,on_delete=models.CASCADE)
    scores = models.IntegerField(default=0)
    resultofquestion = models.CharField(max_length=200)

class Time(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField()


