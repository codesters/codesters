from django.conf.urls import patterns, include, url

from tracks.views import *

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
)
