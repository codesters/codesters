from django.conf.urls import patterns, include, url

from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codesters.views.home', name='home'),
    # url(r'^codesters/', include('codesters.foo.urls')),

    url(r'^$', direct_to_template, {'template': 'index.html' }),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
