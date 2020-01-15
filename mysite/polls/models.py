from django.db import models
#https://docs.djangoproject.com/en/2.2/topics/db/models/
import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    #Question has a question and a publication date.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def my_dumb_method(self):
        return "this is my dumb method."


class Choice(models.Model):
    #Each Choice is associated with a Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #Choice has two fields: the text of the choice and a vote tally.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
