from django.conf.urls import patterns, include, url

from profiles.views import *

urlpatterns = patterns('',
    url(r'^$', MyProfileView.as_view(), name='my_profile'),
    url(r'^blog/$', MyBlogView.as_view(), name='my_blog'),
    url(r'^feeds/$', MyFeedsView.as_view(), name='my_feeds'),
    url(r'^settings/$', MySettingsView.as_view(), name='my_settings'), #Redirects to userprofile_update
    url(r'^tracks/$', MyTracksView.as_view(), name='my_tracks'),
    url(r'^projects/$', MyProjectsView.as_view(), name='my_projects'),
    url(r'^(?P<pk>\d+)/$', UserDetailView.as_view(), name='user_detail'),
    url(r'^(?P<pk>\d+)/settings/core/$', UserUpdateView.as_view(), name='user_update'),
    url(r'^(?P<pk>\d+)/settings/info/$', UserProfileUpdateView.as_view(), name='userprofile_update'), #takes UserProfile pk
    url(r'^(?P<pk>\d+)/feeds/$', UserFeedsView.as_view(), name='user_feeds'),
    url(r'^(?P<pk>\d+)/projects/$', UserProjectsView.as_view(), name='user_projects'),
    url(r'^(?P<pk>\d+)/entries/$', UserEntriesView.as_view(), name='user_entries'),
)
