from django.conf.urls import patterns, include, url

from django.views.generic.simple import direct_to_template

from codesters.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codesters.views.home', name='home'),
    # url(r'^codesters/', include('codesters.foo.urls')),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile/$', ProfileView.as_view(), name='user_profile'),
)
