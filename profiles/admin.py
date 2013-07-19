from django.contrib import admin
from .models import UserProfile, Snippet, Project, Badge, SavedResource, TopicFollow

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

import djadmin2

class UserAdmin2(djadmin2.ModelAdmin2):
    create_form_class = UserCreationForm
    update_form_class = UserChangeForm

class SnippetAdmin(admin.ModelAdmin):
    list_display=('show', 'title', 'user', )
    list_display_links = ['title']
    list_editable = ['show']
    date_hierarchy = 'created_at'
    list_filter = ['show']
    search_fields = ['title', 'content']

class ProjectAdmin(admin.ModelAdmin):
    list_display=('title', 'user', )
    search_fields = ['title', 'description', 'url', 'source_url']

djadmin2.default.register(User, UserAdmin2)
djadmin2.default.register(UserProfile)
admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Badge)
admin.site.register(SavedResource)
admin.site.register(TopicFollow)
