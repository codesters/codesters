from collections import Counter
from urlparse import urlparse
from django.views.generic import TemplateView, ListView
from braces.views import SetHeadlineMixin
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.db.models import Count
from django.contrib.auth.models import User
from resources.models import Topic, Resource

def popular_domains_mixin(number='more'):
    resources = Resource.objects.all()
    cnt = Counter()
    domains = []
    for resource in resources:
        domains.append(urlparse(resource.url)[1])
    for domain in domains:
        cnt[domain] += 1
    if number=='less':
        return cnt.most_common(5)
    else:
        return cnt.most_common()


class PopularTopicListView(SetHeadlineMixin, ListView):
    context_object_name = 'popular_topics'
    template_name = 'explore/explore_all_topics.html'
    headline = 'Topics by Popularity'

    def get_queryset(self):
        return Topic.objects.annotate(no_of_resources=Count('resource')).order_by('-no_of_resources')


class PopularDomainListView(SetHeadlineMixin, ListView):
    context_object_name = 'popular_domains'
    template_name = 'explore/explore_all_domains.html'
    headline = 'All Domains by Popularity'

    def get_queryset(self):
        return popular_domains_mixin()


class RecentResourceListView(SetHeadlineMixin, ListView):
    context_object_name = 'resources'
    template_name = 'explore/explore_all_recent_resources.html'
    headline = 'Recent Resources'

    def get_queryset(self):
        return Resource.objects.all().order_by('-created_at')[:50]


def explore_home(request):
    active_users = User.objects.annotate(no_of_resources=Count('resource')).order_by('-no_of_resources')
    popular_topics = Topic.objects.annotate(no_of_resources=Count('resource')).order_by('-no_of_resources')

    recent_resources = Resource.objects.all().order_by('-created_at')[:5]
    popular_resources = Resource.objects.all().order_by('-rating_votes')[:5]

    ctx = {
            'active_users': active_users[:4],
            'popular_topics': popular_topics[:5],
            'popular_domains': popular_domains_mixin(number='less'),
            'recent_resources': recent_resources,
            'popular_resources': popular_resources,
            'headline': 'Explore'
    }
    return render_to_response('explore/explore_home.html', ctx, context_instance=RequestContext(request))

class ExploreView(SetHeadlineMixin, TemplateView):
    template_name = 'coming_soon.html'
    headline = 'Explore - Coming Soon'


class HomeView(SetHeadlineMixin, TemplateView):
    template_name = 'index.html'
    headline = 'Welcome'


class AboutView(SetHeadlineMixin, TemplateView):
    template_name = 'about.html'
    headline = 'About Us'


class ContactView(SetHeadlineMixin, TemplateView):
    template_name = 'contact.html'
    headline = 'Contact Us'


class GuidelinesView(SetHeadlineMixin, TemplateView):
    template_name = 'guidelines.html'
    headline = 'Guidelines'
