
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lesson(models.Model):
		title = models.CharField(max_length=100)
		image = models.ImageField(upload_to="Lessons")
		award = models.IntegerField()
		description = models.TextField()

		def __unicode__(self):
			return u'%s' % (self.title)

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

class CodeResource(Resource):
		contentFirst = models.TextField()
		contentSecond = models.TextField()
		lang = models.CharField(max_length=50)

class WebResource(Resource):
		location = models.URLField()

class DemoResource(Resource):
		location = models.URLField()

class PictureResource(Resource):
		location = models.ImageField(upload_to="Resources")

class VideoResource(Resource):
		location = models.URLField()

