from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^shop/', include('shop.urls')),
    url(r'^accounts/login/', 'django.contrib.auth.views.login'),
)
