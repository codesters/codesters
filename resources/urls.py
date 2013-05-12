from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

from resources.views import *

urlpatterns = patterns('',
    url(r'^$', resource_home, name='resource_home'),
    url(r'^type/(?P<slug>[-\w]+)/$', RedirectView.as_view(url='/resource/', permanent=True), name='old_resource_list'),
#    url(r'^all/$', ResourceAllListView.as_view(), name='resource_list'),
    url(r'^topic/(?P<slug>[-\w]+)/$', topic_home, name='resource_topic_home'),
    url(r'^topic/(?P<slug>[-\w]+)/all/$', ResourceTopicListView.as_view(), name='resource_topic_list_all'),
    url(r'^topic/(?P<slug>[-\w]+)/(?P<res_type>[-\w]+)/$', ResourceTopicListView.as_view(), name='resource_topic_list'),
    url(r'^(?P<pk>\d+)/$', ResourceDetailView.as_view(), name='resource_detail'),
    #url(r'^(?P<pk>\d+)/save/$', ResourceSaveView.as_view(), name='resource_save'),
    url(r'^save/$', resource_save, name='resource_save'),
    url(r'^(?P<pk>\d+)/edit/$', ResourceUpdateView.as_view(), name='resource_update'),
    url(r'^new/$', ResourceCreateView.as_view(), name='resource_create'),
    url(r'^rate/(?P<object_id>\d+)/(?P<score>\d+)/$', login_required(rate_resource), name='resource_rate'),
)
