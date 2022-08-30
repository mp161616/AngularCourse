from django.contrib import admin
from .models import Quiz, Question, CourseUser, Answer, Result, Section


# Register your models here.

class AnswerInLine(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine, ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

admin.site.register(Quiz)
admin.site.register(CourseUser)
admin.site.register(Result)
admin.site.register(Section)
