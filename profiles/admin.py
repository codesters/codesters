from django.contrib import admin
from profiles.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=('user', 'github_username')

admin.site.register(Student, StudentAdmin)
