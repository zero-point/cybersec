#!/usr/bin/env python

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

################################################################################
# Lessson Model
#
# Storing details on a lesson (ie name, award, description, etc)
# Also stores the code for the demonstrations
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

################################################################################
# Student Model
#
# Storing details on a student (ie name, lessons completed, total points etc)
class Student(models.Model):
		identity = models.OneToOneField(User)
		lessons = models.ManyToManyField(Lesson,blank=True,related_name="lessons")
		completed = models.ManyToManyField(Lesson,blank=True,related_name="completed")
		points = models.IntegerField(default=0,editable=False)

		def __unicode__(self):
			return u'%s %s' % (self.identity.first_name,self.identity.last_name)

class Resource(models.Model):
		name = models.CharField(max_length=100)
		description = models.TextField()
		parent = models.ForeignKey(Lesson)

		def __unicode__(self):
			return u'%s for %s lesson' % (self.name, self.parent.title)

		class Meta:
			abstract = True;

class PictureResource(Resource):
		location = models.ImageField(upload_to="Resources")

