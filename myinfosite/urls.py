from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from shopinfo.views import search

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myinfosite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', search),
)
