from django.contrib import admin
from blog.models import Blog, Tag, Post

class BlogAdmin(admin.ModelAdmin):
    list_display=('title', 'student')

class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'blog', 'created_at', 'published')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
