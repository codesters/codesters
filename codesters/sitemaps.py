from django.contrib.sitemaps import GenericSitemap
from resources.models import Resource, Topic

resource_dict = {
        'queryset': Resource.objects.filter(show=True),
        'date_field': 'updated_at',
}
topic_dict = {
        'queryset': Topic.objects.all(),
}

sitemaps = {
    'topic': GenericSitemap(topic_dict, priority=0.8),
    'resource': GenericSitemap(resource_dict, priority=0.6),
}

