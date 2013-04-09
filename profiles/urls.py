from django.conf.urls import patterns, include, url

from profiles.views import *

urlpatterns = patterns('',
    url(r'^$', MyProfileView.as_view(), name='my_profile'),
#    url(r'^wall/$', MyWallView.as_view(), name='my_wall'),
    url(r'^resources/$', MyResourcesView.as_view(), name='my_resources'),
    url(r'^settings/$', MySettingsView.as_view(), name='my_settings'), #Redirects to userprofile_update
    url(r'^tracks/$', MyTracksView.as_view(), name='my_tracks'),
    url(r'^projects/$', MyProjectsView.as_view(), name='my_projects'),
    url(r'^(?P<username>[\w-]+)/$', user_redirect_view, name='user_detail'),
    url(r'^(?P<username>\w+)/info/$', UserInfoView.as_view(), name='user_info'),
    url(r'^(?P<username>\w+)/resources/$', UserResourcesView.as_view(), name='user_resources'),
    url(r'^(?P<username>\w+)/projects/$', UserProjectsView.as_view(), name='user_projects'),
    url(r'^(?P<username>\w+)/snippets/$', UserSnippetsView.as_view(), name='user_snippets'),
    url(r'^(?P<username>\w+)/snippets/new/$', SnippetCreateView.as_view(), name='create_snippet'),
#    url(r'^(?P<pk>\d+)/settings/wall/$', WallUpdateView.as_view(), name='wall_update'),
    url(r'^(?P<username>\w+)/settings/core/$', UserUpdateView.as_view(), name='user_update'),
    url(r'^(?P<username>\w+)/settings/info/$', UserProfileUpdateView.as_view(), name='userprofile_update'), #takes UserProfile pk
)
