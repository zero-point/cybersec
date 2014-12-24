#!/usr/bin/env python

"""
urls.py

Parsing URLs from user requests

"""

ifrom django.conf.urls import patterns, url
from student import views

urlpatterns = patterns('',
    url(r'^$', views.students, name='students'),
    url(r'^profile', views.student_profile, name='student_profile'),
    url(r'^edit_profile', views.edit_profile, name='edit_profile'),
)     
