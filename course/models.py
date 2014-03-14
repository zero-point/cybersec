#!/usr/bin/env python

"""
models.py

Creating model classes to store lessons, students, website resources, etc...

"""

__author__      = "Arnas Binkauskas, Donald Martin, Josh McGhee & Irina Preda"
__copyright__   = "Copyright 2014, University of Glasgow, Team P"
__version__     = "1.0"
__status__      = "Development"

from django.db import models
from django.contrib.auth.models import User

# Lesson Model -----------------------------------------------------------------
#
# Storing a lesson's name, logo, award & links to required resources

class Lesson(models.Model):
		title           = models.CharField(max_length=100)
		image           = models.ImageField(upload_to="Lessons")
		award           = models.IntegerField()
		description     = models.TextField()
		
		intro           = models.TextField()
		implementation  = models.TextField()
		prevention      = models.TextField()
		
		implementDemo   = models.TextField()
		preventDemo     = models.TextField()

		def __unicode__(self):
			return u'%s' % (self.title)


# Resource Model ---------------------------------------------------------------
#
# Storing website resources, such as links to projects

class Resource(models.Model):
		name        = models.CharField(max_length=100)
		description = models.TextField()
		parent      = models.ForeignKey(Lesson)

		def __unicode__(self):
			return u'%s for %s lesson' % (self.name, self.parent.title)

		class Meta:
			abstract = True;
			
# Picture Resource -------------------------------------------------------------
#
# Subset of resource to store website images.

class PictureResource(Resource):
		location = models.ImageField(upload_to="Resources")

# Web Resource -----------------------------------------------------------------
#
# Subset of resource to store links to other websites.

class WebResource(Resource):
        location = models.URLField()
        
# Housekeepiny -----------------------------------------------------------------

class LessonCompletions(models.Model):
    user    = models.ForeignKey(User)
    lesson  = models.ForeignKey(Lesson)
