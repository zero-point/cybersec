#!/usr/bin/env python

"""
views.py

Getting requests from users and forwarding them onto the appropriate page

"""

__author__      = "Arnas Binkauskas, Donald Martin, Josh McGhee & Irina Preda"
__copyright__   = "Copyright 2014, University of Glasgow, Team P"
__version__     = "1.0"
__status__      = "Development"

from django.http import HttpResponse
from django.template import RequestContext, loader
from course.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate
from django.shortcuts import redirect

# List of Lessons --------------------------------------------------------------
#
# Check that a user is logged in & display the webpage of lessons

@login_required
def lessons(request):
	allLessons      = Lesson.objects.all()
	template        = loader.get_template('course/lessons.html')
	authenticater   = request.user.is_authenticated()
	
	context         = RequestContext(request,
	                                    {'lessons': allLessons,
	                                     'authenticated':authenticater,
	                                })
	
	return HttpResponse(template.render(context))

# Lesson Page ------------------------------------------------------------------
#
# Check that user is logged in & forward to that lesson's page

@login_required
def lesson_page(request):
    lesson          = Lesson.objects.get(title = request.GET.get("title", "NULL"))
    template        = loader.get_template('course/lessonpage.html')
    authenticater   = request.user.is_authenticated()
    
    context         = RequestContext(request, {'resources':lesson,
                                               'authenticated':authenticater,})
    
    return HttpResponse(template.render(context))
    
# Logout User ------------------------------------------------------------------
#
# Check that user is logged in & log them out from the system

@login_required
def logout_user(request):
    logout(request)
    return redirect("lessons")
