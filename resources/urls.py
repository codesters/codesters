from django.conf.urls import patterns, include, url

from resources.views import *

urlpatterns = patterns('',
    url(r'^$', resource_home, name='resource_home'),
    url(r'^type/(?P<slug>[-\w]+)/$', ResourceListView.as_view(), name='resource_list'),
    url(r'^topic/(?P<slug>[-\w]+)/$', ResourceTopicListView.as_view(), name='resource_topic_list'),
    url(r'^r/(?P<pk>\d+)/$', ResourceRedirectView.as_view(), name='resource_redirect'),
    url(r'^(?P<pk>\d+)/$', ResourceDetailView.as_view(), name='resource_detail'),
    url(r'^(?P<pk>\d+)/edit/$', ResourceUpdateView.as_view(), name='resource_update'),
    url(r'^new/$', ResourceCreateView.as_view(), name='resource_create'),
)
