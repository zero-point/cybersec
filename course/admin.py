#!/usr/bin/env python

"""
admin.py

Displays widgets on the administration page.

"""

__author__      = "Arnas Binkauskas, Donald Martin, Josh McGhee & Irina Preda"
__copyright__   = "Copyright 2014, University of Glasgow, Team P"
__version__     = "1.0"
__status__      = "Development"

from django.contrib import admin
from course.models import *

# Admin Page Widgets -----------------------------------------------------------

admin.site.register(Lesson)
admin.site.register(Student)
admin.site.register(PictureResource)
