from django.contrib import admin
from blog.models import Blog, Tag, Entry

class BlogAdmin(admin.ModelAdmin):
    list_display=('title', 'student')

class EntryAdmin(admin.ModelAdmin):
    list_display=('title', 'blog', 'created_at', 'published')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)
