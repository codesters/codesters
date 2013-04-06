from django.contrib import admin
from resources.models import ResourceType, Topic, Resource

class ResourceTypeAdmin(admin.ModelAdmin):
    list_display=('name', 'color')
    prepopulated_fields = {'slug': ['name',]}

class TopicAdmin(admin.ModelAdmin):
    list_display=('name',)
    prepopulated_fields = {'slug': ['name',]}

class ResourceAdmin(admin.ModelAdmin):
    list_display=('title', 'resource_type', 'url')


admin.site.register(ResourceType, ResourceTypeAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Resource, ResourceAdmin)
