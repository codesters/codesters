from django.contrib import admin
from .models import ResourceType, Topic, Resource, FeaturedResource

class ResourceTypeAdmin(admin.ModelAdmin):
    list_display=('name', 'color')
    prepopulated_fields = {'slug': ['name',]}

class TopicAdmin(admin.ModelAdmin):
    list_display=('name',)
    prepopulated_fields = {'slug': ['name',]}

class ResourceAdmin(admin.ModelAdmin):
    list_display=('title', 'resource_type', 'created_by', 'url')
    list_filter = ['resource_type', 'show']
    date_hierarchy = 'created_at'
    search_fields = ['title', 'description', 'url']

class FeaturedResourceAdmin(admin.ModelAdmin):
    list_display=('topic', 'resource_type', 'resource')


admin.site.register(ResourceType, ResourceTypeAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(FeaturedResource, FeaturedResourceAdmin)
