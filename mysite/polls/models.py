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
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #these was_published_recently.foobar lines enable sorting in web page (part7
    #refer https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    #Each Choice is associated with a Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #Choice has two fields: the text of the choice and a vote tally.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
