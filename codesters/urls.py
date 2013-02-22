from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codesters.views.home', name='home'),
    # url(r'^codesters/', include('codesters.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
