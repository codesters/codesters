from django.contrib import admin
from profiles.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user', 'github', 'twitter')

admin.site.register(UserProfile, UserProfileAdmin)
