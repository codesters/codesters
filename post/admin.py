from django.contrib import admin
from post.models import PostType, Tag, Post

class PostTypeAdmin(admin.ModelAdmin):
    list_display=('name',)

class TagAdmin(admin.ModelAdmin):
    list_display=('name',)

class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'url')


admin.site.register(PostType, PostTypeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
