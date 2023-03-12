from django.contrib import admin
#Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

#QuestionInline and ChoiceInline classes

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 3

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


# Register your models here.

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'total_learners', 'full_time')

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date', 'description', 'instructor')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Learner)
admin.site.register(Submission)



