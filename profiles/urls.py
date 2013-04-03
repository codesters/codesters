from django.conf.urls import patterns, include, url

from profiles.views import *

urlpatterns = patterns('',
    url(r'^$', MyProfileView.as_view(), name='user_profile'),
    url(r'^tracks/$', MyTracksView.as_view(), name='user_tracks'),
    url(r'^projects/$', MyProjectsView.as_view(), name='user_projects'),
    url(r'^feeds/$', MyFeedsView.as_view(), name='user_feeds'),
    url(r'^(?P<pk>\d+)/$', StudentProfileView.as_view(), name='student_profile'),
)
