from django.contrib import admin
from track.models import Lesson, Exercise, Post, ExerciseSubmission

class LessonAdmin(admin.ModelAdmin):
    list_display=('name',)

class ExerciseAdmin(admin.ModelAdmin):
    list_display=('name',)

class ExerciseSubmissionAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'student', 'github_url',)

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(ExerciseSubmission, ExerciseSubmissionAdmin)
