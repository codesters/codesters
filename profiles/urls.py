from django.conf.urls import patterns, include, url

from .views import *
from .feeds import UserRecentSnippetsRss, UserRecentSnippetsAtom

urlpatterns = patterns('',
    url(r'^$', MyProfileView.as_view(), name='my_profile'),
    url(r'^resources/$', MyResourcesView.as_view(), name='my_resources'),
    url(r'^(?P<username>[\w.@+-]+)/$', user_redirect_view, name='user_detail'),
    url(r'^(?P<username>[\w.@+-]+)/info/$', UserInfoView.as_view(), name='user_info'),
    url(r'^(?P<username>[\w.@+-]+)/resources/$', UserResourcesView.as_view(), name='user_resources'),
    url(r'^(?P<username>[\w.@+-]+)/projects/$', UserProjectsView.as_view(), name='user_projects'),
    url(r'^(?P<username>[\w.@+-]+)/project/new/$', ProjectCreateView.as_view(), name='project_create'),
    url(r'^(?P<username>[\w.@+-]+)/project/(?P<pk>\d+)/edit/$', ProjectUpdateView.as_view(), name='project_update'),
    url(r'^(?P<username>[\w.@+-]+)/project/(?P<pk>\d+)/delete/$', ProjectDeleteView.as_view(), name='project_delete'),
    url(r'^(?P<username>[\w.@+-]+)/snippets/$', UserSnippetsView.as_view(), name='user_snippets'),
    url(r'^(?P<username>[\w.@+-]+)/snippets/rss/$', UserRecentSnippetsRss(), name='user_snippet_rss'),
    url(r'^(?P<username>[\w.@+-]+)/snippets/atom/$', UserRecentSnippetsAtom(), name='user_snippet_atom'),
    url(r'^(?P<username>[\w.@+-]+)/snippets/new/$', SnippetCreateView.as_view(), name='snippet_create'),
    url(r'^(?P<username>[\w.@+-]+)/snippets/(?P<pk>\d+)/$', SnippetDetailView.as_view(), name='snippet_detail'),
    url(r'^(?P<username>[\w.@+-]+)/snippets/(?P<pk>\d+)/edit/$', SnippetUpdateView.as_view(), name='snippet_update'),
    url(r'^(?P<username>[\w.@+-]+)/snippets/(?P<pk>\d+)/delete/$', SnippetDeleteView.as_view(), name='snippet_delete'),
)
