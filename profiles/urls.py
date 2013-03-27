from django.conf.urls import patterns, include, url

from profiles.views import *

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', StudentDetailView.as_view(), name='student_detail'),
)
