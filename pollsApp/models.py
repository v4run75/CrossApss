import datetime

from django.utils import timezone
from django.db import models


class Question(models.Model):
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Customer(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    contact = models.CharField(max_length=50, unique=True)
    # description= models.CharField(max_length=10)
