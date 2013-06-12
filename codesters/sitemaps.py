from django.contrib.sitemaps import GenericSitemap
from resources.models import Resource, Topic
from profiles.models import Snippet

resource_dict = {
        'queryset': Resource.objects.filter(show=True),
        'date_field': 'updated_at',
}
topic_dict = {
        'queryset': Topic.objects.all(),
}
snippet_dict = {
        'queryset': Snippet.objects.filter(show=True),
        'date_field': 'updated_at',
}

sitemaps = {
    'topic': GenericSitemap(topic_dict, priority=0.8),
    'resource': GenericSitemap(resource_dict, priority=0.6),
    'snippet': GenericSitemap(snippet_dict, priority=0.6),
}

