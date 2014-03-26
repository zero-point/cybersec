#!/usr/bin/env python

"""
urls.py

Parsing URLs from user requests

"""

__author__      = "Arnas Binkauskas, Donald Martin, Josh McGhee & Irina Preda"
__copyright__   = "Copyright 2014, University of Glasgow, Team P"
__version__     = "1.0"
__status__      = "Development"

from django.conf.urls import patterns, url
from student import views

urlpatterns = patterns('',
    url(r'^$', views.students, name='students'),
    url(r'^profile', views.student_profile, name='student_profile'),
    url(r'^edit_profile', views.edit_profile, name='edit_profile'),
)     
