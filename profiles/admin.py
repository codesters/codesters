from django.contrib import admin
from .models import UserProfile, Snippet, Project, SavedResource, TopicFollow

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'receive_email',)
    search_fields = ('user', 'bio', 'gravatar_email', 'twitter', 'stackoverflow', 'facebook', 'website', 'receive_email')


class SavedResourceAdmin(admin.ModelAdmin):
    list_display = ('user', 'resource', 'saved_at')
    date_hierarchy = 'saved_at'

class TopicFollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic', 'followed_at')
    date_hierarchy = 'followed_at'

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
admin.site.register(SavedResource, SavedResourceAdmin)
admin.site.register(TopicFollow, TopicFollowAdmin)
