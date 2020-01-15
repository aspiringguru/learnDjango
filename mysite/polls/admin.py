from django.contrib import admin

# Register your models here.
from .models import Choice, Question

#StackedInline takes more vertical space
#TabularInline stacks horizontally.
#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice  #Choice class as imported from polls/models.py
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    #add a bunch of Choices directly when you create the Question object.
    inlines = [ChoiceInline]
    #this used when url = /admin/polls/question/
    #NBB: list_display can include class attributes and methods
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    #list_filter adds filter to select any/today/7 days/month/year
    search_fields = ['question_text']
    #https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
#import & register class Question defined in the app model file
#file polls/models.py has > class Question(models.Model):
