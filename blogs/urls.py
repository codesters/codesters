from django.conf.urls import patterns, include, url

from blogs.views import *

urlpatterns = patterns('',
    url(r'^new/$', EntryCreateView.as_view(), name='entry_create'),
    url(r'^(?P<username>\w+)/$', EntryListView.as_view(), name='blog_detail'),
    url(r'^(?P<username>\w+)/(?P<slug>[-\w]+)/$', EntryDetailView.as_view(), name='entry_detail'),
    url(r'^(?P<username>\w+)/(?P<slug>[-\w]+)/$', EntryDetailView.as_view(), name='entry_detail'),
    url(r'^(?P<username>\w+)/(?P<slug>[-\w]+)/edit/$', EntryUpdateView.as_view(), name='entry_update'),
    url(r'^$', BlogHomeView.as_view(), name='blog_home'),
)
