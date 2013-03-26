from django.contrib import admin
from post.models import PostType, Tag, Post

class PostTypeAdmin(admin.ModelAdmin):
    list_display=('name',)
    prepopulated_fields = {'slug': ['name',]}

class TagAdmin(admin.ModelAdmin):
    list_display=('name',)
    prepopulated_fields = {'slug': ['name',]}

class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'post_type', 'url')


admin.site.register(PostType, PostTypeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
