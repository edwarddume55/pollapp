from django.contrib import admin

# Register your models here.
from .models import Question,Choice

admin.site.site_header="Pollapp Admin"
admin.site.site_title="Pollapp Admin Area"
admin.site.index_title="Welcome to the PollApp Admin Area"

class ChoiceInLine(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['question_text']}), ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInLine]

admin.site.register(Question,QuestionAdmin)