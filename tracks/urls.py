from django.conf.urls import patterns, include, url

from tracks.views import *

urlpatterns = patterns('',
    url(r'^$', TrackHomeView.as_view(), name='track_list'),
)
