from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Snippet

class RecentSnippetsRss(Feed):
    title = "Recent Snippets on Codesters"
    description = "Provides feed for recent snippets shared on codesters.org"
    description_template = "feeds/snippets.html"

    def items(self):
        return Snippet.objects.order_by('-created_at')

    def item_title(self, item):
        return item.title


class RecentSnippetsAtom(RecentSnippetsRss):
    feed_type = Atom1Feed
    subtitle = RecentSnippetsRss.description


class UserRecentSnippetsRss(Feed):
    description_template = "feeds/snippets.html"

    def get_object(self, request, username):
        return get_object_or_404(User, username=username)

    def title(self, obj):
        return "Recent snippets from %s" %obj.username

    def link(self, obj):
        return obj.get_absolute_url()

    def description(self, obj):
        return "feed for recent snippets shared on codesters from %s" %obj.username

    def items(self, obj):
        return obj.snippet_set.all().order_by('-created_at')

    def item_title(self, item):
        return item.title


class UserRecentSnippetsAtom(UserRecentSnippetsRss):
    feed_type = Atom1Feed
    subtitle = UserRecentSnippetsRss.description
