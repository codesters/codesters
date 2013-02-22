from django.contrib import admin
from profiles.models import Student, Moderator

class StudentAdmin(admin.ModelAdmin):
    list_display=('user',)

class ModeratorAdmin(admin.ModelAdmin):
    list_display=('user',)

admin.site.register(Student, StudentAdmin)
admin.site.register(Moderator, ModeratorAdmin)
