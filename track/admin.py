from django.contrib import admin
from track.models import Lesson, Exercise, Post

class LessonAdmin(admin.ModelAdmin):
    list_display=('name',)

class ExerciseAdmin(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Exercise, ExerciseAdmin)
