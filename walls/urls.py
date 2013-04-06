from django.conf.urls import patterns, include, url

from walls.views import *

#TODO rethink wall app urls
urlpatterns = patterns('',
    url(r'^new/$', SnippetCreateView.as_view(), name='snippet_create'),
    url(r'^(?P<pk>\d+)/$', SnippetListView.as_view(), name='wall_detail'),
    url(r'^snippet/(?P<pk>\d+)/$', SnippetDetailView.as_view(), name='snippet_detail'),
    url(r'^snippet/(?P<pk>\d+)/edit/$', SnippetUpdateView.as_view(), name='snippet_update'),
    url(r'^$', WallHomeView.as_view(), name='wall_home'),
)
