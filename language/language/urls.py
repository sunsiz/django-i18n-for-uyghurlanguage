from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'language.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'uyghur.views.home', name='home'),
)
