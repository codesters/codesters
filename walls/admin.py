from django.contrib import admin
from walls.models import Wall, Tag, Snippet

class WallAdmin(admin.ModelAdmin):
    list_display=('title', 'user')
    list_display_link = ['title']
    search_fields = ['title', 'subtitle', 'user']
    prepopulated_fields = {'slug': ['title',]}


class SnippetAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('title', 'wall', 'created_at', 'published')
    list_display_link = ['title', 'wall']
    list_editable = ['published']
    list_filter = ['published','updated_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ['title',]}


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_link = ['name']
    prepopulated_fields = {'slug': ['name',]}


admin.site.register(Wall, WallAdmin)
admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Tag, TagAdmin)
