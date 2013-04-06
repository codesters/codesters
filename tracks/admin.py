from django.contrib import admin
from tracks.models import Badge, Chapter, Track, TrackCategory, Exercise, ExerciseSubmission

class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_by')
    prepopulated_fields = {'slug':('name',)}

class TrackCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug':('name',)}

class ChapterAdmin(admin.ModelAdmin):
    list_display=('name', 'track')
    prepopulated_fields = {'slug':('name',)}

class ExerciseAdmin(admin.ModelAdmin):
    list_display=('title',)

class ExerciseSubmissionAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'student', 'github_url',)

class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'track')

admin.site.register(Track, TrackAdmin)
admin.site.register(TrackCategory, TrackCategoryAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(ExerciseSubmission, ExerciseSubmissionAdmin)
admin.site.register(Badge, BadgeAdmin)
