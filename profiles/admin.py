from django.contrib import admin
from .models import UserProfile, Snippet, Project, Badge, SavedResource, TopicFollow

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user', )

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

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Badge)
admin.site.register(SavedResource)
admin.site.register(TopicFollow)
