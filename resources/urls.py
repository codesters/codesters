from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import RedirectView

from .views import *
from .feeds import RecentResourcesRss, TopicRecentResourcesRss, RecentResourcesAtom, TopicRecentResourcesAtom


urlpatterns = patterns('',
    url(r'^$', resource_home, name='resource_home'),
    url(r'^rss/$', RecentResourcesRss(), name='resource_feed_rss'),
    url(r'^atom/$', RecentResourcesAtom(), name='resource_feed_atom'),
    url(r'^topic/new/$', permission_required('resources.add_topic', raise_exception=True)(TopicCreateView.as_view()), name='topic_create'),
    url(r'^topic/(?P<slug>[-\w]+)/$', topic_home, name='resource_topic_home'),
    url(r'^topic/(?P<slug>[-\w]+)/edit/$', TopicUpdateView.as_view(), name='topic_update'),
    url(r'^topic/(?P<topic_slug>[-\w]+)/rss/$', TopicRecentResourcesRss(), name='topic_feed_rss'),
    url(r'^topic/(?P<topic_slug>[-\w]+)/atom/$', TopicRecentResourcesAtom(), name='topic_feed_atom'),
    url(r'^topic/(?P<slug>[-\w]+)/follow/$', TopicFollowView.as_view(), name='topic_follow'),
    url(r'^topic/(?P<slug>[-\w]+)/all/$', ResourceTopicListView.as_view(), name='resource_topic_list_all'),
    url(r'^topic/(?P<slug>[-\w]+)/offline/$', RedirectView.as_view(url='/resource/', permanent=True)), #Removed offline resource_type
    url(r'^topic/(?P<slug>[-\w]+)/documentation/$', RedirectView.as_view(url='/resource/', permanent=True)), #Removed documentation resource_type
    url(r'^topic/(?P<slug>[-\w]+)/(?P<res_type>[-\w]+)/$', ResourceTopicListView.as_view(), name='resource_topic_list'),
    url(r'^(?P<pk>\d+)/$', ResourceDetailView.as_view(), name='resource_detail'),
    url(r'^(?P<pk>\d+)/save/$', ResourceSaveView.as_view(), name='resource_save'),
    url(r'^(?P<pk>\d+)/feature/(?P<slug>[-\w]+)/$', ResourceFeatureView.as_view(), name='resource_feature'),
    url(r'^(?P<pk>\d+)/edit/$', ResourceUpdateView.as_view(), name='resource_update'),
    url(r'^new/$', ResourceCreateView.as_view(), name='resource_create'),
    url(r'^rate/(?P<object_id>\d+)/(?P<score>\d+)/$', login_required(rate_resource), name='resource_rate'),
)
