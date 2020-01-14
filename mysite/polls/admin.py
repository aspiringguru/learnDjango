from django.contrib import admin

# Register your models here.
from .models import Question

admin.site.register(Question)
#import & register class Question defined in the app model file
#file polls/models.py has > class Question(models.Model):
