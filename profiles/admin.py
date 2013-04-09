from django.contrib import admin
from profiles.models import UserProfile, Snippet, Project, Badge

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user', )

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Snippet)
admin.site.register(Project)
admin.site.register(Badge)
