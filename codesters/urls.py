from django.conf.urls import patterns, include, url

from django.views.generic.simple import direct_to_template

from codesters.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='page_home'),
    url(r'^about/$', AboutView.as_view(), name='page_about'),
    url(r'^team/$', TeamView.as_view(), name='page_team'),
    url(r'^contact/$', ContactView.as_view(), name='page_contact'),
    url(r'^guidelines/$', GuidelinesView.as_view(), name='page_guidelines'),
    url(r'^accounts/profile/$', ProfileView.as_view(), name='user_profile'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^blog/', include('blogs.urls')),
    url(r'^feed/', include('feeds.urls')),
    url(r'^profile/', include('profiles.urls')),
)
