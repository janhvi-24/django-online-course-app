from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content', 'course', 'grade']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
# Register other models as needed
