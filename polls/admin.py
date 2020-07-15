from django.contrib import admin

# Register your models here.

from .models import Question, Choice

admin.site.site_header = "WaitTime"
admin.site.site_title = "WaitTime"
admin.site.index_title = "Welcome Admin"

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ["pub_date"], 'classes': ['collapse']}),
    ]
    
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)

