from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceInline(admin.StackedInline):
    model = Choice  #Choice class as imported from polls/models.py
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    #fields = ['question_text', 'pub_date']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    #add a bunch of Choices directly when you create the Question object.
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
#import & register class Question defined in the app model file
#file polls/models.py has > class Question(models.Model):
