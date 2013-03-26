from django.conf.urls import patterns, include, url

from post.views import *

urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^popular/$', PostPopularListView.as_view(), name='post_popular_list'),
    url(r'^type/(?P<slug>[-\w]+)/$', PostTypeListView.as_view(), name='post_type_list'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
)
