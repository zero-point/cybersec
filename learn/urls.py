#!/usr/bin/env python

"""
urls.py

Parsing URLs from user requests

"""

from django.conf.urls import patterns, include, url
from course import views
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from learn import settings
from django.views.generic import RedirectView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lessons/', include('course.urls')),
    url(r'^register/individual', views.register_individual, name='register_individual'),
    url(r'^brainstorm/', views.brainstorm, name='brainstorm'),
    url(r'^tutorial/', views.tutorial, name='tutorial'),
    url(r'^$', views.index, name='index'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
