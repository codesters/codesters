from django.contrib import admin
from feeds.models import FeedType, Tag, Feed

class FeedTypeAdmin(admin.ModelAdmin):
    list_display=('name', 'color')
    prepopulated_fields = {'slug': ['name',]}

class TagAdmin(admin.ModelAdmin):
    list_display=('name',)
    prepopulated_fields = {'slug': ['name',]}

class FeedAdmin(admin.ModelAdmin):
    list_display=('title', 'feed_type', 'url')


admin.site.register(FeedType, FeedTypeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Feed, FeedAdmin)
