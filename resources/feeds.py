from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.shortcuts import get_object_or_404
from .models import Resource, Topic

class RecentResourcesRss(Feed):
    title = "Recent Resources on Codesters"
    link = "/resource/"
    description = "Provides feed for recent resources shared on codesters.org"
    description_template = "feeds/resources.html"

    def items(self):
        return Resource.objects.order_by('-created_at')[:10]

    def item_title(self, item):
        return item.title


class RecentResourcesAtom(RecentResourcesRss):
    feed_type = Atom1Feed
    subtitle = RecentResourcesRss.description


class TopicRecentResourcesRss(Feed):
    description_template = "feeds/resources.html"

    def get_object(self, request, topic_slug):
        return get_object_or_404(Topic, slug=topic_slug)

    def title(self, obj):
        return "Recent resources for %s" %obj.name

    def link(self, obj):
        return obj.get_absolute_url()

    def description(self, obj):
        return "feed for recent resources shared on codesters for %s" %obj.name

    def items(self, obj):
        return obj.resource_set.all().order_by('-created_at')[:10]

    def item_title(self, item):
        return item.title


class TopicRecentResourcesAtom(TopicRecentResourcesRss):
    feed_type = Atom1Feed
    subtitle = TopicRecentResourcesRss.description
