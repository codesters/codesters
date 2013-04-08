from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from codesters.views import *

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='page_home'),
    url(r'^about/$', AboutView.as_view(), name='page_about'),
    url(r'^team/$', TeamView.as_view(), name='page_team'),
    url(r'^contact/$', ContactView.as_view(), name='page_contact'),
    url(r'^guidelines/$', GuidelinesView.as_view(), name='page_guidelines'),
    url(r'^explore/$', ExploreView.as_view(), name='explore_home'),
    url(r'^users/(?P<username>[\w-]+)/$', user_redirect_view, name='user_redirect'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^wall/', include('walls.urls')),
    url(r'^resource/', include('resources.urls')),
    url(r'^profile/', include('profiles.urls')),
#    url(r'^track/', include('tracks.urls')),
    url(r'^track/', TrackHomeView.as_view(), name='track_list'),
)
