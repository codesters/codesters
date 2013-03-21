from django.contrib import admin
from blog.models import Blog, Tag, Entry

class BlogAdmin(admin.ModelAdmin):
    list_display=('title', 'user')
    list_display_link = ['title']
    search_fields = ['title', 'user']


class EntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    fields = ('published', 'title', 'blog', 'slug', 'content')
    list_display = ('title', 'blog', 'created_at', 'published')
    list_display_link = ['title', 'blog']
    list_editable = ['published']
    list_filter = ['published','updated_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ['title',]}


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_link = ['name']
    prepopulated_fields = {'slug': ['name',]}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag, TagAdmin)
